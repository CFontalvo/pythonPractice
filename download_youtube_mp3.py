import argparse
from pathlib import Path

import yt_dlp


def download_mp3(url: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(output_dir / "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Descarga el audio de un video de YouTube en MP3."
    )
    parser.add_argument("url", help="URL del video de YouTube")
    parser.add_argument(
        "--output-dir",
        default="MP3",
        help="Carpeta destino para los MP3 (por defecto: MP3)",
    )
    args = parser.parse_args()

    download_mp3(args.url, Path(args.output_dir))


if __name__ == "__main__":
    main()
