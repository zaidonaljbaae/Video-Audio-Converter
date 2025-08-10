import os
import sys
import threading
import queue
import time
import shutil
import tkinter as tk
import ffmpeg

from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk 

AUTHOR_NAME = "Zaidon Aljbaae"
APP_TITLE = "Video → MP3 Converter"
DEFAULT_BITRATE = "192k"
VIDEO_EXTS = (".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".m4v", ".webm")

USING_TTKBOOTSTRAP = False
try:
    import ttkbootstrap as tb  # type: ignore
    USING_TTKBOOTSTRAP = True
except Exception:
    pass

OUTPUT_FORMATS = {
    "mp3":  {"codec": "libmp3lame"},
    "wav":  {"codec": "pcm_s16le"},
    "aac":  {"codec": "aac"},
    "ogg":  {"codec": "libvorbis"},
    "flac": {"codec": "flac"},
    "m4a":  {"codec": "aac"},
    "opus": {"codec": "libopus"},
}

def resource_path(rel: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base, rel)

REL_FFMPEG = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "ffmpeg", "bin",
    "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
)

def _probe_ffmpeg(cmd: str) -> bool:
    try:
        (ffmpeg
         .input("anullsrc", f="lavfi", t=0.1)
         .output("nul" if os.name == "nt" else "/dev/null", f="mp3")
         .run(cmd=cmd, overwrite_output=True, quiet=True))
        return True
    except Exception:
        return False

def resolve_ffmpeg() -> str:
    candidates = [
        resource_path(os.path.join("ffmpeg", "bin", "ffmpeg.exe" if os.name == "nt" else "ffmpeg")),
        REL_FFMPEG,
        shutil.which("ffmpeg") or ""
    ]
    seen, unique = set(), []
    for c in candidates:
        c = os.path.normpath(c) if c else c
        if c and c not in seen:
            seen.add(c)
            unique.append(c)
    for cmd in unique:
        if (os.path.isfile(cmd) or shutil.which(cmd)) and _probe_ffmpeg(cmd):
            return cmd
    return ""

def next_available_filename(path: str) -> str:
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    while True:
        candidate = f"{base} ({i}){ext}"
        if not os.path.exists(candidate):
            return candidate
        i += 1

class ConverterApp((tb.Window if USING_TTKBOOTSTRAP else tk.Tk)):  # type: ignore
    def __init__(self):
        if USING_TTKBOOTSTRAP:
            super().__init__(themename="flatly")
        else:
            super().__init__()
        self.title(APP_TITLE)
        self.geometry("840x560")
        self.minsize(560, 380)
        self.resizable(True, True)

        try:
            self.iconbitmap(resource_path("icon.ico"))
        except Exception:
            pass

        self.video_files: list[str] = []
        self.output_dir = ""
        self.bitrate = tk.StringVar(value=DEFAULT_BITRATE)
        self.use_source_dir = tk.BooleanVar(value=False)
        self.ffmpeg_cmd = ""
        self.task_queue: "queue.Queue[tuple[str,str]]" = queue.Queue()
        self._build_ui()

        self.after(120, self._check_ffmpeg_on_start)
        self.after(120, self._poll_queue)

    # ---------- UI ----------
    def _build_ui(self):
        # Root layout: three vertical blocks that resize nicely
        root = ttk.Frame(self)
        root.pack(fill="both", expand=True)
        root.grid_columnconfigure(0, weight=1)
        for r in (0, 1, 2, 3):
            root.grid_rowconfigure(r, weight=0)
        root.grid_rowconfigure(4, weight=1)   # log area expands
        root.grid_rowconfigure(5, weight=0)   # footer

        # Header
        hdr = ttk.Frame(root)
        hdr.grid(row=0, column=0, sticky="ew", padx=14, pady=(14, 4))

        ttk.Label(hdr, text="Video Converter", font=("Segoe UI", 16, "bold")).pack(side="left")

        # Source files
        frm_src = ttk.LabelFrame(root, text="Source Videos")
        frm_src.grid(row=1, column=0, sticky="nsew", padx=14, pady=8)
        frm_src.grid_columnconfigure(0, weight=1)
        frm_src.grid_rowconfigure(0, weight=1)

        inner_src = ttk.Frame(frm_src)
        inner_src.grid(row=0, column=0, sticky="nsew", padx=12, pady=10)
        inner_src.grid_columnconfigure(0, weight=1)
        inner_src.grid_rowconfigure(0, weight=1)

        self.lst_files = tk.Listbox(inner_src, height=6, selectmode=tk.EXTENDED, activestyle="dotbox")
        self.lst_files.grid(row=0, column=0, rowspan=3, sticky="nsew")
        sb = ttk.Scrollbar(inner_src, orient="vertical", command=self.lst_files.yview)
        sb.grid(row=0, column=1, rowspan=3, sticky="ns")
        self.lst_files.configure(yscrollcommand=sb.set)

        btns = ttk.Frame(inner_src)
        btns.grid(row=0, column=2, rowspan=3, sticky="nsw", padx=(10, 0))
        ttk.Button(btns, text="Add Files…", command=self.add_files).pack(fill="x", pady=(0, 6))
        ttk.Button(btns, text="Remove Selected", command=self.remove_selected).pack(fill="x", pady=6)
        ttk.Button(btns, text="Clear List", command=self.clear_list).pack(fill="x", pady=(6, 0))

        # Output options
        frm_out = ttk.LabelFrame(root, text="Output")
        frm_out.grid(row=2, column=0, sticky="ew", padx=14, pady=8)
        inner_out = ttk.Frame(frm_out)
        inner_out.pack(fill="both", expand=True, padx=12, pady=10)
        inner_out.grid_columnconfigure(3, weight=1)

        ttk.Label(inner_out, text="Bitrate:").grid(row=0, column=0, sticky="w")
        self.cmb_bitrate = ttk.Combobox(inner_out, textvariable=self.bitrate,
                                        values=["128k", "192k", "256k", "320k"],
                                        width=8, state="readonly")
        self.cmb_bitrate.grid(row=0, column=1, sticky="w", padx=(6, 20))

        ttk.Label(inner_out, text="Format:").grid(row=0, column=2, sticky="w")
        self.format_var = tk.StringVar(value="mp3")
        self.cmb_format = ttk.Combobox(
            inner_out, textvariable=self.format_var,
            values=list(OUTPUT_FORMATS.keys()), width=6, state="readonly"
        )
        self.cmb_format.grid(row=0, column=3, sticky="w", padx=(6, 20))

        self.chk_same = ttk.Checkbutton(
            inner_out, text="Save next to source files",
            variable=self.use_source_dir, command=self._toggle_outdir_controls
        )
        self.chk_same.grid(row=0, column=4, sticky="w")

        # Output folder
        ttk.Label(inner_out, text="Output Folder:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.ent_outdir = ttk.Entry(inner_out)

        # NEW: Set default text to current working directory
        default_dir = os.getcwd()
        self.output_dir = default_dir
        self.ent_outdir.insert(0, default_dir)

        self.ent_outdir.grid(row=1, column=1, columnspan=3, sticky="ew", pady=(10, 0))
        ttk.Button(inner_out, text="Browse…", command=self.choose_output_dir)\
            .grid(row=1, column=4, padx=(10, 0), pady=(10, 0))

        self._toggle_outdir_controls()

        # Controls
        ctrl = ttk.Frame(root)
        ctrl.grid(row=3, column=0, sticky="ew", padx=14, pady=(6, 2))
        self.btn_convert = ttk.Button(ctrl, text="Convert", command=self.start_conversion)
        self.btn_convert.pack(side="left")
        ttk.Button(ctrl, text="Open Output Folder", command=self.open_output_dir)\
            .pack(side="left", padx=(10, 0))

        # Progress + Logs (this area expands)
        bottom = ttk.Frame(root)
        bottom.grid(row=4, column=0, sticky="nsew", padx=14, pady=(4, 6))
        bottom.grid_columnconfigure(0, weight=1)
        bottom.grid_rowconfigure(1, weight=1)
        self.prg = ttk.Progressbar(bottom, mode="indeterminate")
        self.prg.grid(row=0, column=0, sticky="ew")
        self.txt_log = tk.Text(bottom, height=6, wrap="none")
        self.txt_log.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        self.txt_log.config(state="disabled")

        # Footer with visible clickable links (fixed)
        footer = ttk.Frame(root)
        footer.grid(row=5, column=0, sticky="ew", padx=14, pady=(0, 10))
        footer.grid_columnconfigure(0, weight=1)

        email = "zaidonaljbaae@gmail.com"
        link_color = "blue"  # visible on light/dark; ttkbootstrap won’t intercept

        def open_mail(_event=None):
            import webbrowser
            webbrowser.open(f"mailto:{email}?subject=Support%20Request")

        def hover_on(lbl):
            lbl.configure(font=("Segoe UI", 9, "underline"))

        def hover_off(lbl):
            lbl.configure(font=("Segoe UI", 9))

        created_by = tk.Label(
            footer, text="Created by Zaidon Aljbaae",
            fg=link_color, cursor="hand2", font=("Segoe UI", 9)
        )
        created_by.grid(row=0, column=0, sticky="w")
        created_by.bind("<Button-1>", open_mail)
        created_by.bind("<Enter>", lambda e: hover_on(created_by))
        created_by.bind("<Leave>", lambda e: hover_off(created_by))

        email_lbl = tk.Label(
            footer, text=f"Email: {email}",
            fg=link_color, cursor="hand2", font=("Segoe UI", 9)
        )
        email_lbl.grid(row=0, column=1, sticky="e")
        email_lbl.bind("<Button-1>", open_mail)
        email_lbl.bind("<Enter>", lambda e: hover_on(email_lbl))
        email_lbl.bind("<Leave>", lambda e: hover_off(email_lbl))


    # ---------- Helpers ----------
    def log(self, msg: str):
        self.txt_log.config(state="normal")
        self.txt_log.insert("end", f"{time.strftime('%H:%M:%S')}  {msg}\n")
        self.txt_log.see("end")
        self.txt_log.config(state="disabled")

    def _toggle_outdir_controls(self):
        state = "disabled" if self.use_source_dir.get() else "normal"
        self.ent_outdir.config(state=state)

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Select Video Files",
            filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv *.m4v *.webm")]
        )
        if not files:
            return
        added = 0
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext not in VIDEO_EXTS:
                continue
            if f not in self.video_files:
                self.video_files.append(f)
                self.lst_files.insert("end", os.path.basename(f))
                added += 1
        self.log(f"Added {added} file(s).")

    def remove_selected(self):
        selected = list(self.lst_files.curselection())
        if not selected:
            return
        for idx in reversed(selected):
            if 0 <= idx < len(self.video_files):
                self.video_files.pop(idx)
            self.lst_files.delete(idx)
        self.log("Removed selected file(s).")

    def clear_list(self):
        self.video_files.clear()
        self.lst_files.delete(0, "end")
        self.log("Cleared file list.")

    def choose_output_dir(self):
        d = filedialog.askdirectory(title="Select Output Folder")
        if d:
            self.output_dir = d
            self.ent_outdir.delete(0, "end")
            self.ent_outdir.insert(0, d)
            # NEW: switch to explicit output folder mode
            self.use_source_dir.set(False)
            self._toggle_outdir_controls()
            self.log(f"Output folder set to: {d}")

    def open_output_dir(self):
        target = None
        if self.use_source_dir.get():
            if self.video_files:
                target = os.path.dirname(self.video_files[0])
        else:
            target = self.ent_outdir.get().strip() or self.output_dir
        if target and os.path.isdir(target):
            if sys.platform.startswith("win"):
                os.startfile(target)  # type: ignore
            elif sys.platform == "darwin":
                os.system(f'open "{target}"')
            else:
                os.system(f'xdg-open "{target}"')
        else:
            messagebox.showinfo("Info", "No valid output folder to open.")

    def _check_ffmpeg_on_start(self):
        self.ffmpeg_cmd = resolve_ffmpeg()
        if self.ffmpeg_cmd:
            pass
        else:
            self.log("FFmpeg not detected. (Bundle it or place ./ffmpeg/bin/ffmpeg.exe)")
            messagebox.showwarning(
                "FFmpeg not found",
                "FFmpeg was not detected. Bundle it via PyInstaller --add-binary, "
                "or place ffmpeg under ./ffmpeg/bin/."
            )

    def _poll_queue(self):
        try:
            while True:
                msg, level = self.task_queue.get_nowait()
                if level == "log":
                    self.log(msg)
                elif level == "error":
                    self.log(f"[ERROR] {msg}")
                    messagebox.showerror("Error", msg)
                elif level == "done":
                    self.log(msg)
                    messagebox.showinfo("Done", msg)
                    self.prg.stop()
                    self.btn_convert.config(state="normal")
        except queue.Empty:
            pass
        finally:
            self.after(150, self._poll_queue)

    # ---------- Conversion ----------
    def start_conversion(self):
        if not self.video_files:
            messagebox.showerror("Error", "Add at least one video file.")
            return

        save_next_to_source = self.use_source_dir.get()
        outdir = ""
        if not save_next_to_source:
            outdir = self.ent_outdir.get().strip()
            if not outdir:
                messagebox.showerror("Error", "Choose an output folder or enable 'Save next to source'.")
                return
            if not os.path.isdir(outdir):
                try:
                    os.makedirs(outdir, exist_ok=True)
                except Exception as e:
                    messagebox.showerror("Error", f"Cannot create output folder:\n{e}")
                    return

        self.ffmpeg_cmd = resolve_ffmpeg()
        if not self.ffmpeg_cmd:
            messagebox.showerror("Error", "FFmpeg not detected. Bundle it or place it under ./ffmpeg/bin/.")
            return

        self.btn_convert.config(state="disabled")
        self.prg.start(10)
        threading.Thread(
            target=self._worker_convert,
            args=(self.video_files.copy(), save_next_to_source, outdir, self.bitrate.get(), self.ffmpeg_cmd),
            daemon=True
        ).start()

    def _worker_convert(self, files, save_next_to_source, outdir, bitrate, custom_cmd):
        ok, fail = 0, 0
        out_format = self.format_var.get()
        codec = OUTPUT_FORMATS[out_format]["codec"]

        for src in files:
            try:
                if not os.path.isfile(src):
                    raise RuntimeError("Source file not found.")
                dst_dir = os.path.dirname(src) if save_next_to_source else outdir
                base = os.path.splitext(os.path.basename(src))[0]
                dst = next_available_filename(os.path.join(dst_dir, f"{base}.{out_format}"))
                self.task_queue.put((f"Converting: {os.path.basename(src)} → {os.path.basename(dst)} @ {bitrate}", "log"))
                stream = ffmpeg.input(src)

                if out_format in ["wav", "flac", "ogg", "opus"]:
                    stream = stream.output(dst, format=out_format, acodec=codec)
                elif out_format == "aac":
                    stream = stream.output(dst, format="adts", acodec="aac", audio_bitrate=bitrate, ac=2, ar=44100)
                elif out_format == "m4a":
                    stream = stream.output(dst, format="mp4", acodec="aac", audio_bitrate=bitrate, ac=2, ar=44100)
                else:
                    stream = stream.output(dst, format=out_format, acodec=codec, audio_bitrate=bitrate)

                try:
                    stream.run(cmd=custom_cmd, overwrite_output=True, capture_stderr=True)
                    ok += 1
                    self.task_queue.put((f"Done: {os.path.basename(dst)}", "log"))
                except ffmpeg.Error as fe:
                    error_details = fe.stderr.decode("utf-8", errors="replace") if fe.stderr else str(fe)
                    fail += 1
                    self.task_queue.put((f"Failed: {os.path.basename(src)} — FFmpeg error:\n{error_details}", "error"))
            except Exception as e:
                fail += 1
                self.task_queue.put((f"Failed: {os.path.basename(src)} — {e}", "error"))

        self.task_queue.put((f"Completed. Success: {ok}, Failed: {fail}.", "done"))

if __name__ == "__main__":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
    app = ConverterApp()
    app.mainloop()
