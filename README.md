# Descargador de música de YouTube (MP3)

Este script descarga el audio de un video de YouTube y lo guarda como `.mp3` en la carpeta `MP3`.

## Requisitos

- Python 3.9+
- `yt-dlp`
- `ffmpeg` instalado y disponible en tu PATH

## Instalación

```bash
pip install yt-dlp
```

## Uso

```bash
python download_youtube_mp3.py "https://www.youtube.com/watch?v=..."
```

Si quieres cambiar la carpeta destino:

```bash
python download_youtube_mp3.py "https://www.youtube.com/watch?v=..." --output-dir MP3
```

Los archivos descargados quedarán en la carpeta `MP3`.
