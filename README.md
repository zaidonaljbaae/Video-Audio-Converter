# Video-Audio-Converter
A simple, fast, and user-friendly desktop app to convert video files to audio (MP3, WAV, AAC, OGG, FLAC, M4A, OPUS) using FFmpeg. Built with Python + Tkinter (optional: ttkbootstrap for a nicer theme).
Features

Add multiple videos and batch convert

Choose output format and bitrate

Save next to source or to a chosen output folder

Progress log with success/failure per file

Auto-detect FFmpeg (bundled, local ./ffmpeg/bin, or system PATH)

Resizable UI (works from tiny window to full screen)

Requirements
Python 3.9+ (tested on 3.11)

Packages:

pip install ffmpeg-python
# optional (nicer theme)
pip install ttkbootstrap
# optional (only if you show a scaled header icon image using PIL)
pip install pillow
FFmpeg

Either in system PATH (ffmpeg command available), or

In ./ffmpeg/bin/ffmpeg.exe (Windows), or

Bundled into your build via PyInstaller (see Build section).

Run from Source 

# (recommended) create and activate a venv
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt  # if you add one
# or manually:
pip install ffmpeg-python ttkbootstrap pillow

python main.py
If the app says “FFmpeg not detected”, either install FFmpeg and add it to PATH, or place it at ./ffmpeg/bin/ffmpeg.exe (Windows). The app will probe and use the first working one it finds.

Build (Windows, PyInstaller One-File)
Goal: A single VideoToMP3.exe that includes FFmpeg inside.
Assuming you put ffmpeg.exe at ./ffmpeg/bin/ffmpeg.exe and your window/taskbar icon is icon.ico.

pyinstaller --onefile --noconsole --icon=icon.ico --name "VideoToMP3" `
  --add-binary ".\ffmpeg\bin\ffmpeg.exe;ffmpeg\bin" `
  --add-data "icon.ico;." `
  main.py
--icon=icon.ico sets the EXE icon (OS/taskbar).

--add-binary bundles FFmpeg so users don’t need to install it.

--add-data "icon.ico;." bundles your icon if you also use it at runtime (optional).

On Windows, use semicolons in --add-data. On macOS/Linux use colons (see below).

The build output will be in dist/VideoToMP3.exe.

Usage
Add Files… to select video files (.mp4, .avi, .mov, .mkv, .flv, .wmv, .m4v, .webm).

Pick Bitrate and Format (MP3 default).

Choose where to save:

Save next to source files (same folder as the videos), or

Uncheck it and set Output Folder (defaults to your current working directory; updates when you click Browse…).

Click Convert. Progress and messages appear in the log.

How FFmpeg Is Found
At startup (and before conversion), the app tries:

Bundled: resource_path("ffmpeg/bin/ffmpeg") (PyInstaller one-file/one-folder)

Local: ./ffmpeg/bin/ffmpeg(.exe)

System PATH: shutil.which("ffmpeg")

It probes FFmpeg by running a tiny null conversion. If it works, it uses that path.

Notes
ttkbootstrap is optional. The app works with plain Tk if not installed.

Pillow is only needed if you’re resizing/embedding a header icon image inside the GUI.
The window/taskbar icon uses iconbitmap and does not require Pillow.

