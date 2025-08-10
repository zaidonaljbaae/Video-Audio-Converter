FFmpeg 64-bit static Windows build from www.gyan.dev

Version: 2025-08-07-git-fa458c7243-essentials_build-www.gyan.dev

License: GPL v3

Source Code: https://github.com/FFmpeg/FFmpeg/commit/fa458c7243

git-essentials build configuration: 

ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          yes
makeinfo supports HTML    yes
xmllint enabled           yes

External libraries:
avisynth                libopencore_amrnb       libvpx
bzlib                   libopencore_amrwb       libwebp
gmp                     libopenjpeg             libx264
gnutls                  libopenmpt              libx265
iconv                   libopus                 libxml2
libaom                  librubberband           libxvid
libass                  libspeex                libzimg
libfontconfig           libsrt                  libzmq
libfreetype             libssh                  lzma
libfribidi              libtheora               mediafoundation
libgme                  libvidstab              openal
libgsm                  libvmaf                 sdl2
libharfbuzz             libvo_amrwbenc          zlib
libmp3lame              libvorbis

External libraries providing hardware acceleration:
amf                     d3d12va                 nvdec
cuda                    dxva2                   nvenc
cuda_llvm               ffnvcodec               vaapi
cuvid                   libmfx
d3d11va                 libvpl

Libraries:
avcodec                 avformat                swscale
avdevice                avutil
avfilter                swresample

Programs:
ffmpeg                  ffplay                  ffprobe

Enabled decoders:
aac                     fourxm                  pfm
aac_fixed               fraps                   pgm
aac_latm                frwu                    pgmyuv
aasc                    ftr                     pgssub
ac3                     g2m                     pgx
ac3_fixed               g723_1                  phm
acelp_kelvin            g728                    photocd
adpcm_4xm               g729                    pictor
adpcm_adx               gdv                     pixlet
adpcm_afc               gem                     pjs
adpcm_agm               gif                     png
adpcm_aica              gremlin_dpcm            ppm
adpcm_argo              gsm                     prores
adpcm_ct                gsm_ms                  prosumer
adpcm_dtk               h261                    psd
adpcm_ea                h263                    ptx
adpcm_ea_maxis_xa       h263i                   qcelp
adpcm_ea_r1             h263p                   qdm2
adpcm_ea_r2             h264                    qdmc
adpcm_ea_r3             h264_amf                qdraw
adpcm_ea_xas            h264_cuvid              qoa
adpcm_g722              h264_qsv                qoi
adpcm_g726              hap                     qpeg
adpcm_g726le            hca                     qtrle
adpcm_ima_acorn         hcom                    r10k
adpcm_ima_alp           hdr                     r210
adpcm_ima_amv           hevc                    ra_144
adpcm_ima_apc           hevc_amf                ra_288
adpcm_ima_apm           hevc_cuvid              ralf
adpcm_ima_cunning       hevc_qsv                rasc
adpcm_ima_dat4          hnm4_video              rawvideo
adpcm_ima_dk3           hq_hqa                  realtext
adpcm_ima_dk4           hqx                     rka
adpcm_ima_ea_eacs       huffyuv                 rl2
adpcm_ima_ea_sead       hymt                    roq
adpcm_ima_iss           iac                     roq_dpcm
adpcm_ima_moflex        idcin                   rpza
adpcm_ima_mtf           idf                     rscc
adpcm_ima_oki           iff_ilbm                rtv1
adpcm_ima_qt            ilbc                    rv10
adpcm_ima_rad           imc                     rv20
adpcm_ima_smjpeg        imm4                    rv30
adpcm_ima_ssi           imm5                    rv40
adpcm_ima_wav           indeo2                  rv60
adpcm_ima_ws            indeo3                  s302m
adpcm_ima_xbox          indeo4                  sami
adpcm_ms                indeo5                  sanm
adpcm_mtaf              interplay_acm           sbc
adpcm_psx               interplay_dpcm          scpr
adpcm_sanyo             interplay_video         screenpresso
adpcm_sbpro_2           ipu                     sdx2_dpcm
adpcm_sbpro_3           jacosub                 sga
adpcm_sbpro_4           jpeg2000                sgi
adpcm_swf               jpegls                  sgirle
adpcm_thp               jv                      sheervideo
adpcm_thp_le            kgv1                    shorten
adpcm_vima              kmvc                    simbiosis_imx
adpcm_xa                lagarith                sipr
adpcm_xmd               lead                    siren
adpcm_yamaha            libaom_av1              smackaud
adpcm_zork              libgsm                  smacker
agm                     libgsm_ms               smc
aic                     libopencore_amrnb       smvjpeg
alac                    libopencore_amrwb       snow
alias_pix               libopus                 sol_dpcm
als                     libspeex                sonic
amrnb                   libvorbis               sp5x
amrwb                   libvpx_vp8              speedhq
amv                     libvpx_vp9              speex
anm                     loco                    srgc
ansi                    lscr                    srt
anull                   m101                    ssa
apac                    mace3                   stl
ape                     mace6                   subrip
apng                    magicyuv                subviewer
aptx                    mdec                    subviewer1
aptx_hd                 media100                sunrast
apv                     metasound               svq1
arbc                    microdvd                svq3
argo                    mimic                   tak
ass                     misc4                   targa
asv1                    mjpeg                   targa_y216
asv2                    mjpeg_cuvid             tdsc
atrac1                  mjpeg_qsv               text
atrac3                  mjpegb                  theora
atrac3al                mlp                     thp
atrac3p                 mmvideo                 tiertexseqvideo
atrac3pal               mobiclip                tiff
atrac9                  motionpixels            tmv
aura                    movtext                 truehd
aura2                   mp1                     truemotion1
av1                     mp1float                truemotion2
av1_amf                 mp2                     truemotion2rt
av1_cuvid               mp2float                truespeech
av1_qsv                 mp3                     tscc
avrn                    mp3adu                  tscc2
avrp                    mp3adufloat             tta
avs                     mp3float                twinvq
avui                    mp3on4                  txd
bethsoftvid             mp3on4float             ulti
bfi                     mpc7                    utvideo
bink                    mpc8                    v210
binkaudio_dct           mpeg1_cuvid             v210x
binkaudio_rdft          mpeg1video              v308
bintext                 mpeg2_cuvid             v408
bitpacked               mpeg2_qsv               v410
bmp                     mpeg2video              vb
bmv_audio               mpeg4                   vble
bmv_video               mpeg4_cuvid             vbn
bonk                    mpegvideo               vc1
brender_pix             mpl2                    vc1_cuvid
c93                     msa1                    vc1_qsv
cavs                    mscc                    vc1image
cbd2_dpcm               msmpeg4v1               vcr1
ccaption                msmpeg4v2               vmdaudio
cdgraphics              msmpeg4v3               vmdvideo
cdtoons                 msnsiren                vmix
cdxl                    msp2                    vmnc
cfhd                    msrle                   vnull
cinepak                 mss1                    vorbis
clearvideo              mss2                    vp3
cljr                    msvideo1                vp4
cllc                    mszh                    vp5
comfortnoise            mts2                    vp6
cook                    mv30                    vp6a
cpia                    mvc1                    vp6f
cri                     mvc2                    vp7
cscd                    mvdv                    vp8
cyuv                    mvha                    vp8_cuvid
dca                     mwsc                    vp8_qsv
dds                     mxpeg                   vp9
derf_dpcm               nellymoser              vp9_amf
dfa                     notchlc                 vp9_cuvid
dfpwm                   nuv                     vp9_qsv
dirac                   on2avc                  vplayer
dnxhd                   opus                    vqa
dolby_e                 osq                     vqc
dpx                     paf_audio               vvc
dsd_lsbf                paf_video               vvc_qsv
dsd_lsbf_planar         pam                     wady_dpcm
dsd_msbf                pbm                     wavarc
dsd_msbf_planar         pcm_alaw                wavpack
dsicinaudio             pcm_bluray              wbmp
dsicinvideo             pcm_dvd                 wcmv
dss_sp                  pcm_f16le               webp
dst                     pcm_f24le               webvtt
dvaudio                 pcm_f32be               wmalossless
dvbsub                  pcm_f32le               wmapro
dvdsub                  pcm_f64be               wmav1
dvvideo                 pcm_f64le               wmav2
dxa                     pcm_lxf                 wmavoice
dxtory                  pcm_mulaw               wmv1
dxv                     pcm_s16be               wmv2
eac3                    pcm_s16be_planar        wmv3
eacmv                   pcm_s16le               wmv3image
eamad                   pcm_s16le_planar        wnv1
eatgq                   pcm_s24be               wrapped_avframe
eatgv                   pcm_s24daud             ws_snd1
eatqi                   pcm_s24le               xan_dpcm
eightbps                pcm_s24le_planar        xan_wc3
eightsvx_exp            pcm_s32be               xan_wc4
eightsvx_fib            pcm_s32le               xbin
escape124               pcm_s32le_planar        xbm
escape130               pcm_s64be               xface
evrc                    pcm_s64le               xl
exr                     pcm_s8                  xma1
fastaudio               pcm_s8_planar           xma2
ffv1                    pcm_sga                 xpm
ffvhuff                 pcm_u16be               xsub
ffwavesynth             pcm_u16le               xwd
fic                     pcm_u24be               y41p
fits                    pcm_u24le               ylc
flac                    pcm_u32be               yop
flashsv                 pcm_u32le               yuv4
flashsv2                pcm_u8                  zero12v
flic                    pcm_vidc                zerocodec
flv                     pcx                     zlib
fmvc                    pdv                     zmbv

Enabled encoders:
a64multi                hevc_d3d12va            pcm_u16le
a64multi5               hevc_mf                 pcm_u24be
aac                     hevc_nvenc              pcm_u24le
aac_mf                  hevc_qsv                pcm_u32be
ac3                     hevc_vaapi              pcm_u32le
ac3_fixed               huffyuv                 pcm_u8
ac3_mf                  jpeg2000                pcm_vidc
adpcm_adx               jpegls                  pcx
adpcm_argo              libaom_av1              pfm
adpcm_g722              libgsm                  pgm
adpcm_g726              libgsm_ms               pgmyuv
adpcm_g726le            libmp3lame              phm
adpcm_ima_alp           libopencore_amrnb       png
adpcm_ima_amv           libopenjpeg             ppm
adpcm_ima_apm           libopus                 prores
adpcm_ima_qt            libspeex                prores_aw
adpcm_ima_ssi           libtheora               prores_ks
adpcm_ima_wav           libvo_amrwbenc          qoi
adpcm_ima_ws            libvorbis               qtrle
adpcm_ms                libvpx_vp8              r10k
adpcm_swf               libvpx_vp9              r210
adpcm_yamaha            libwebp                 ra_144
alac                    libwebp_anim            rawvideo
alias_pix               libx264                 roq
amv                     libx264rgb              roq_dpcm
anull                   libx265                 rpza
apng                    libxvid                 rv10
aptx                    ljpeg                   rv20
aptx_hd                 magicyuv                s302m
ass                     mjpeg                   sbc
asv1                    mjpeg_qsv               sgi
asv2                    mjpeg_vaapi             smc
av1_amf                 mlp                     snow
av1_mf                  movtext                 speedhq
av1_nvenc               mp2                     srt
av1_qsv                 mp2fixed                ssa
av1_vaapi               mp3_mf                  subrip
avrp                    mpeg1video              sunrast
avui                    mpeg2_qsv               svq1
bitpacked               mpeg2_vaapi             targa
bmp                     mpeg2video              text
cfhd                    mpeg4                   tiff
cinepak                 msmpeg4v2               truehd
cljr                    msmpeg4v3               tta
comfortnoise            msrle                   ttml
dca                     msvideo1                utvideo
dfpwm                   nellymoser              v210
dnxhd                   opus                    v308
dpx                     pam                     v408
dvbsub                  pbm                     v410
dvdsub                  pcm_alaw                vbn
dvvideo                 pcm_bluray              vc2
dxv                     pcm_dvd                 vnull
eac3                    pcm_f32be               vorbis
exr                     pcm_f32le               vp8_vaapi
ffv1                    pcm_f64be               vp9_qsv
ffvhuff                 pcm_f64le               vp9_vaapi
fits                    pcm_mulaw               wavpack
flac                    pcm_s16be               wbmp
flashsv                 pcm_s16be_planar        webvtt
flashsv2                pcm_s16le               wmav1
flv                     pcm_s16le_planar        wmav2
g723_1                  pcm_s24be               wmv1
gif                     pcm_s24daud             wmv2
h261                    pcm_s24le               wrapped_avframe
h263                    pcm_s24le_planar        xbm
h263p                   pcm_s32be               xface
h264_amf                pcm_s32le               xsub
h264_mf                 pcm_s32le_planar        xwd
h264_nvenc              pcm_s64be               y41p
h264_qsv                pcm_s64le               yuv4
h264_vaapi              pcm_s8                  zlib
hdr                     pcm_s8_planar           zmbv
hevc_amf                pcm_u16be

Enabled hwaccels:
av1_d3d11va             hevc_nvdec              vc1_nvdec
av1_d3d11va2            hevc_vaapi              vc1_vaapi
av1_d3d12va             mjpeg_nvdec             vp8_nvdec
av1_dxva2               mjpeg_vaapi             vp8_vaapi
av1_nvdec               mpeg1_nvdec             vp9_d3d11va
av1_vaapi               mpeg2_d3d11va           vp9_d3d11va2
h263_vaapi              mpeg2_d3d11va2          vp9_d3d12va
h264_d3d11va            mpeg2_d3d12va           vp9_dxva2
h264_d3d11va2           mpeg2_dxva2             vp9_nvdec
h264_d3d12va            mpeg2_nvdec             vp9_vaapi
h264_dxva2              mpeg2_vaapi             vvc_vaapi
h264_nvdec              mpeg4_nvdec             wmv3_d3d11va
h264_vaapi              mpeg4_vaapi             wmv3_d3d11va2
hevc_d3d11va            vc1_d3d11va             wmv3_d3d12va
hevc_d3d11va2           vc1_d3d11va2            wmv3_dxva2
hevc_d3d12va            vc1_d3d12va             wmv3_nvdec
hevc_dxva2              vc1_dxva2               wmv3_vaapi

Enabled parsers:
aac                     dvd_nav                 mpeg4video
aac_latm                dvdsub                  mpegaudio
ac3                     evc                     mpegvideo
adx                     ffv1                    opus
amr                     flac                    png
apv                     ftr                     pnm
av1                     g723_1                  qoi
avs2                    g729                    rv34
avs3                    gif                     sbc
bmp                     gsm                     sipr
cavsvideo               h261                    tak
cook                    h263                    vc1
cri                     h264                    vorbis
dca                     hdr                     vp3
dirac                   hevc                    vp8
dnxhd                   ipu                     vp9
dnxuc                   jpeg2000                vvc
dolby_e                 jpegxl                  webp
dpx                     misc4                   xbm
dvaudio                 mjpeg                   xma
dvbsub                  mlp                     xwd

Enabled demuxers:
aa                      idcin                   pcm_mulaw
aac                     idf                     pcm_s16be
aax                     iff                     pcm_s16le
ac3                     ifv                     pcm_s24be
ac4                     ilbc                    pcm_s24le
ace                     image2                  pcm_s32be
acm                     image2_alias_pix        pcm_s32le
act                     image2_brender_pix      pcm_s8
adf                     image2pipe              pcm_u16be
adp                     image_bmp_pipe          pcm_u16le
ads                     image_cri_pipe          pcm_u24be
adx                     image_dds_pipe          pcm_u24le
aea                     image_dpx_pipe          pcm_u32be
afc                     image_exr_pipe          pcm_u32le
aiff                    image_gem_pipe          pcm_u8
aix                     image_gif_pipe          pcm_vidc
alp                     image_hdr_pipe          pdv
amr                     image_j2k_pipe          pjs
amrnb                   image_jpeg_pipe         pmp
amrwb                   image_jpegls_pipe       pp_bnk
anm                     image_jpegxl_pipe       pva
apac                    image_pam_pipe          pvf
apc                     image_pbm_pipe          qcp
ape                     image_pcx_pipe          qoa
apm                     image_pfm_pipe          r3d
apng                    image_pgm_pipe          rawvideo
aptx                    image_pgmyuv_pipe       rcwt
aptx_hd                 image_pgx_pipe          realtext
apv                     image_phm_pipe          redspark
aqtitle                 image_photocd_pipe      rka
argo_asf                image_pictor_pipe       rl2
argo_brp                image_png_pipe          rm
argo_cvg                image_ppm_pipe          roq
asf                     image_psd_pipe          rpl
asf_o                   image_qdraw_pipe        rsd
ass                     image_qoi_pipe          rso
ast                     image_sgi_pipe          rtp
au                      image_sunrast_pipe      rtsp
av1                     image_svg_pipe          s337m
avi                     image_tiff_pipe         sami
avisynth                image_vbn_pipe          sap
avr                     image_webp_pipe         sbc
avs                     image_xbm_pipe          sbg
avs2                    image_xpm_pipe          scc
avs3                    image_xwd_pipe          scd
bethsoftvid             imf                     sdns
bfi                     ingenient               sdp
bfstm                   ipmovie                 sdr2
bink                    ipu                     sds
binka                   ircam                   sdx
bintext                 iss                     segafilm
bit                     iv8                     ser
bitpacked               ivf                     sga
bmv                     ivr                     shorten
boa                     jacosub                 siff
bonk                    jpegxl_anim             simbiosis_imx
brstm                   jv                      sln
c93                     kux                     smacker
caf                     kvag                    smjpeg
cavsvideo               laf                     smush
cdg                     lc3                     sol
cdxl                    libgme                  sox
cine                    libopenmpt              spdif
codec2                  live_flv                srt
codec2raw               lmlm4                   stl
concat                  loas                    str
dash                    lrc                     subviewer
data                    luodat                  subviewer1
daud                    lvf                     sup
dcstr                   lxf                     svag
derf                    m4v                     svs
dfa                     matroska                swf
dfpwm                   mca                     tak
dhav                    mcc                     tedcaptions
dirac                   mgsts                   thp
dnxhd                   microdvd                threedostr
dsf                     mjpeg                   tiertexseq
dsicin                  mjpeg_2000              tmv
dss                     mlp                     truehd
dts                     mlv                     tta
dtshd                   mm                      tty
dv                      mmf                     txd
dvbsub                  mods                    ty
dvbtxt                  moflex                  usm
dxa                     mov                     v210
ea                      mp3                     v210x
ea_cdata                mpc                     vag
eac3                    mpc8                    vc1
epaf                    mpegps                  vc1t
evc                     mpegts                  vividas
ffmetadata              mpegtsraw               vivo
filmstrip               mpegvideo               vmd
fits                    mpjpeg                  vobsub
flac                    mpl2                    voc
flic                    mpsub                   vpk
flv                     msf                     vplayer
fourxm                  msnwc_tcp               vqf
frm                     msp                     vvc
fsb                     mtaf                    w64
fwse                    mtv                     wady
g722                    musx                    wav
g723_1                  mv                      wavarc
g726                    mvi                     wc3
g726le                  mxf                     webm_dash_manifest
g728                    mxg                     webvtt
g729                    nc                      wsaud
gdv                     nistsphere              wsd
genh                    nsp                     wsvqa
gif                     nsv                     wtv
gsm                     nut                     wv
gxf                     nuv                     wve
h261                    obu                     xa
h263                    ogg                     xbin
h264                    oma                     xmd
hca                     osq                     xmv
hcom                    paf                     xvag
hevc                    pcm_alaw                xwma
hls                     pcm_f32be               yop
hnm                     pcm_f32le               yuv4mpegpipe
iamf                    pcm_f64be
ico                     pcm_f64le

Enabled muxers:
a64                     h263                    pcm_s24be
ac3                     h264                    pcm_s24le
ac4                     hash                    pcm_s32be
adts                    hds                     pcm_s32le
adx                     hevc                    pcm_s8
aea                     hls                     pcm_u16be
aiff                    iamf                    pcm_u16le
alp                     ico                     pcm_u24be
amr                     ilbc                    pcm_u24le
amv                     image2                  pcm_u32be
apm                     image2pipe              pcm_u32le
apng                    ipod                    pcm_u8
aptx                    ircam                   pcm_vidc
aptx_hd                 ismv                    psp
apv                     ivf                     rawvideo
argo_asf                jacosub                 rcwt
argo_cvg                kvag                    rm
asf                     latm                    roq
asf_stream              lc3                     rso
ass                     lrc                     rtp
ast                     m4v                     rtp_mpegts
au                      matroska                rtsp
avi                     matroska_audio          sap
avif                    md5                     sbc
avm2                    microdvd                scc
avs2                    mjpeg                   segafilm
avs3                    mkvtimestamp_v2         segment
bit                     mlp                     smjpeg
caf                     mmf                     smoothstreaming
cavsvideo               mov                     sox
codec2                  mp2                     spdif
codec2raw               mp3                     spx
crc                     mp4                     srt
dash                    mpeg1system             stream_segment
data                    mpeg1vcd                streamhash
daud                    mpeg1video              sup
dfpwm                   mpeg2dvd                swf
dirac                   mpeg2svcd               tee
dnxhd                   mpeg2video              tg2
dts                     mpeg2vob                tgp
dv                      mpegts                  truehd
eac3                    mpjpeg                  tta
evc                     mxf                     ttml
f4v                     mxf_d10                 uncodedframecrc
ffmetadata              mxf_opatom              vc1
fifo                    null                    vc1t
filmstrip               nut                     voc
fits                    obu                     vvc
flac                    oga                     w64
flv                     ogg                     wav
framecrc                ogv                     webm
framehash               oma                     webm_chunk
framemd5                opus                    webm_dash_manifest
g722                    pcm_alaw                webp
g723_1                  pcm_f32be               webvtt
g726                    pcm_f32le               wsaud
g726le                  pcm_f64be               wtv
gif                     pcm_f64le               wv
gsm                     pcm_mulaw               yuv4mpegpipe
gxf                     pcm_s16be
h261                    pcm_s16le

Enabled protocols:
async                   http                    rtmp
cache                   httpproxy               rtmpe
concat                  https                   rtmps
concatf                 icecast                 rtmpt
crypto                  ipfs_gateway            rtmpte
data                    ipns_gateway            rtmpts
fd                      libsrt                  rtp
ffrtmpcrypt             libssh                  srtp
ffrtmphttp              libzmq                  subfile
file                    md5                     tcp
ftp                     mmsh                    tee
gopher                  mmst                    tls
gophers                 pipe                    udp
hls                     prompeg                 udplite

Enabled filters:
a3dscope                datascope               pan
aap                     dblur                   perlin
abench                  dcshift                 perms
abitscope               dctdnoiz                perspective
acompressor             ddagrab                 phase
acontrast               deband                  photosensitivity
acopy                   deblock                 pixdesctest
acrossfade              decimate                pixelize
acrossover              deconvolve              pixscope
acrusher                dedot                   pp7
acue                    deesser                 premultiply
addroi                  deflate                 prewitt
adeclick                deflicker               procamp_vaapi
adeclip                 deinterlace_qsv         pseudocolor
adecorrelate            deinterlace_vaapi       psnr
adelay                  dejudder                pullup
adenorm                 delogo                  qp
aderivative             denoise_vaapi           random
adrawgraph              deshake                 readeia608
adrc                    despill                 readvitc
adynamicequalizer       detelecine              realtime
adynamicsmooth          dialoguenhance          remap
aecho                   dilation                removegrain
aemphasis               displace                removelogo
aeval                   doubleweave             repeatfields
aevalsrc                drawbox                 replaygain
aexciter                drawbox_vaapi           reverse
afade                   drawgraph               rgbashift
afdelaysrc              drawgrid                rgbtestsrc
afftdn                  drawtext                roberts
afftfilt                drmeter                 rotate
afir                    dynaudnorm              rubberband
afireqsrc               earwax                  sab
afirsrc                 ebur128                 scale
aformat                 edgedetect              scale2ref
afreqshift              elbg                    scale_cuda
afwtdn                  entropy                 scale_d3d11
agate                   epx                     scale_qsv
agraphmonitor           eq                      scale_vaapi
ahistogram              equalizer               scdet
aiir                    erosion                 scharr
aintegral               estdif                  scroll
ainterleave             exposure                segment
alatency                extractplanes           select
alimiter                extrastereo             selectivecolor
allpass                 fade                    sendcmd
allrgb                  feedback                separatefields
allyuv                  fftdnoiz                setdar
aloop                   fftfilt                 setfield
alphaextract            field                   setparams
alphamerge              fieldhint               setpts
amerge                  fieldmatch              setrange
ametadata               fieldorder              setsar
amix                    fillborders             settb
amovie                  find_rect               sharpness_vaapi
amplify                 firequalizer            shear
amultiply               flanger                 showcqt
anequalizer             floodfill               showcwt
anlmdn                  format                  showfreqs
anlmf                   fps                     showinfo
anlms                   framepack               showpalette
anoisesrc               framerate               showspatial
anull                   framestep               showspectrum
anullsink               freezedetect            showspectrumpic
anullsrc                freezeframes            showvolume
apad                    fspp                    showwaves
aperms                  fsync                   showwavespic
aphasemeter             gblur                   shuffleframes
aphaser                 geq                     shufflepixels
aphaseshift             gradfun                 shuffleplanes
apsnr                   gradients               sidechaincompress
apsyclip                graphmonitor            sidechaingate
apulsator               grayworld               sidedata
arealtime               greyedge                sierpinski
aresample               guided                  signalstats
areverse                haas                    signature
arls                    haldclut                silencedetect
arnndn                  haldclutsrc             silenceremove
asdr                    hdcd                    sinc
asegment                headphone               sine
aselect                 hflip                   siti
asendcmd                highpass                smartblur
asetnsamples            highshelf               smptebars
asetpts                 hilbert                 smptehdbars
asetrate                histeq                  sobel
asettb                  histogram               spectrumsynth
ashowinfo               hqdn3d                  speechnorm
asidedata               hqx                     split
asisdr                  hstack                  spp
asoftclip               hstack_qsv              sr_amf
aspectralstats          hstack_vaapi            ssim
asplit                  hsvhold                 ssim360
ass                     hsvkey                  stereo3d
astats                  hue                     stereotools
astreamselect           huesaturation           stereowiden
asubboost               hwdownload              streamselect
asubcut                 hwmap                   subtitles
asupercut               hwupload                super2xsai
asuperpass              hwupload_cuda           superequalizer
asuperstop              hysteresis              surround
atadenoise              identity                swaprect
atempo                  idet                    swapuv
atilt                   il                      tblend
atrim                   inflate                 telecine
avectorscope            interlace               testsrc
avgblur                 interleave              testsrc2
avsynctest              join                    thistogram
axcorrelate             kerndeint               threshold
azmq                    kirsch                  thumbnail
backgroundkey           lagfun                  thumbnail_cuda
bandpass                latency                 tile
bandreject              lenscorrection          tiltandshift
bass                    libvmaf                 tiltshelf
bbox                    life                    tinterlace
bench                   limitdiff               tlut2
bilateral               limiter                 tmedian
bilateral_cuda          loop                    tmidequalizer
biquad                  loudnorm                tmix
bitplanenoise           lowpass                 tonemap
blackdetect             lowshelf                tonemap_vaapi
blackframe              lumakey                 tpad
blend                   lut                     transpose
blockdetect             lut1d                   transpose_vaapi
blurdetect              lut2                    treble
bm3d                    lut3d                   tremolo
boxblur                 lutrgb                  trim
bwdif                   lutyuv                  unpremultiply
bwdif_cuda              mandelbrot              unsharp
cas                     maskedclamp             untile
ccrepack                maskedmax               uspp
cellauto                maskedmerge             v360
channelmap              maskedmin               vaguedenoiser
channelsplit            maskedthreshold         varblur
chorus                  maskfun                 vectorscope
chromahold              mcdeint                 vflip
chromakey               mcompand                vfrdet
chromakey_cuda          median                  vibrance
chromanr                mergeplanes             vibrato
chromashift             mestimate               vidstabdetect
ciescope                metadata                vidstabtransform
codecview               midequalizer            vif
color                   minterpolate            vignette
colorbalance            mix                     virtualbass
colorchannelmixer       monochrome              vmafmotion
colorchart              morpho                  volume
colorcontrast           movie                   volumedetect
colorcorrect            mpdecimate              vpp_amf
colordetect             mptestsrc               vpp_qsv
colorhold               msad                    vstack
colorize                multiply                vstack_qsv
colorkey                negate                  vstack_vaapi
colorlevels             nlmeans                 w3fdif
colormap                nnedi                   waveform
colormatrix             noformat                weave
colorspace              noise                   xbr
colorspace_cuda         normalize               xcorrelate
colorspectrum           null                    xfade
colortemperature        nullsink                xmedian
compand                 nullsrc                 xpsnr
compensationdelay       oscilloscope            xstack
concat                  overlay                 xstack_qsv
convolution             overlay_cuda            xstack_vaapi
convolve                overlay_qsv             yadif
copy                    overlay_vaapi           yadif_cuda
corr                    owdenoise               yaepblur
cover_rect              pad                     yuvtestsrc
crop                    pad_cuda                zmq
cropdetect              pad_vaapi               zoneplate
crossfeed               pal100bars              zoompan
crystalizer             pal75bars               zscale
cue                     palettegen
curves                  paletteuse

Enabled bsfs:
aac_adtstoasc           h264_mp4toannexb        pgs_frame_merge
apv_metadata            h264_redundant_pps      prores_metadata
av1_frame_merge         hapqa_extract           remove_extradata
av1_frame_split         hevc_metadata           setts
av1_metadata            hevc_mp4toannexb        showinfo
chomp                   imx_dump_header         text2movsub
dca_core                media100_to_mjpegb      trace_headers
dovi_rpu                mjpeg2jpeg              truehd_core
dts2pts                 mjpega_dump_header      vp9_metadata
dump_extradata          mov2textsub             vp9_raw_reorder
dv_error_marker         mpeg2_metadata          vp9_superframe
eac3_core               mpeg4_unpack_bframes    vp9_superframe_split
evc_frame_merge         noise                   vvc_metadata
extract_extradata       null                    vvc_mp4toannexb
filter_units            opus_metadata
h264_metadata           pcm_rechunk

Enabled indevs:
dshow                   lavfi                   vfwcap
gdigrab                 openal

Enabled outdevs:

git-essentials external libraries' versions: 

AMF v1.4.36-3-gcf4445f
aom v3.12.1-244-g930f7e2b9c
AviSynthPlus v3.7.5-26-g7ae5d480
ffnvcodec n13.0.19.0-1-gf2fb9b3
freetype VER-2-13-3
fribidi v1.0.16-2-gb28f43b
gsm 1.0.22
harfbuzz 11.3.3-409-g3b4336ba
lame 3.100
libass 0.17.4-14-g338fd2c
libgme 0.6.4
libopencore-amrnb 0.1.6
libopencore-amrwb 0.1.6
libssh 0.11.2
libtheora 1.2.0
openal-soft latest
openmpt libopenmpt-0.6.24-11-ga0a41ed1b
opus v1.5.2-161-gf92fdda4
rubberband v1.8.1
SDL release-2.32.0-81-gd310b5679
speex Speex-1.2.1-51-g0589522
srt v1.5.4-37-g5d80411
VAAPI 2.23.0.
vidstab v1.1.1-18-gd9933c1
vmaf v3.0.0-112-gb9ac69e6
vo-amrwbenc 0.1.3
vorbis v1.3.7-10-g84c02369
VPL 2.15
vpx v1.15.2-96-g378952481
x264 v0.165.3222
x265 4.1-191-g8f11c33ac
xvid v1.3.7
zeromq 4.3.5
zimg release-3.0.5-207-g0e56801

