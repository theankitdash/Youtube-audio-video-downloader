# YouTube Media Downloader

A simple Python-based command-line tool for downloading YouTube media using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

The program provides three download options:

* 🎥 **Video only**
* 🎵 **Audio only (MP3)**
* 🎬 **Video + Audio (MP4)**

## Features

* Download videos up to 1080p
* Extract audio as MP3
* Download and merge video + audio
* Simple interactive command-line menu
* Uses `yt-dlp` for reliable media downloading

## Requirements

* Python 3.8+
* `yt-dlp`
* FFmpeg

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/youtube-media-downloader.git
cd youtube-media-downloader
```

### 2. Install yt-dlp

```bash
pip install yt-dlp
```

### 3. Install FFmpeg

FFmpeg is required for:

* Extracting audio as MP3
* Merging separate video and audio streams

On Windows, if you use Chocolatey:

```bash
choco install ffmpeg -y
```

Verify the installation:

```bash
ffmpeg -version
```

## Usage

Run the Python script:

```bash
python youtube_downloader.py
```

Enter the YouTube URL when prompted:

```text
Enter the video URL: https://www.youtube.com/watch?v=XXXXXXXXXXX

What do you want to download?
1. Video only
2. Audio only
3. Video + Audio

Enter your choice (1/2/3):
```

### Options

#### 1. Video Only

Downloads the best available video stream up to 1080p.

```text
Choice: 1
```

#### 2. Audio Only

Downloads the best available audio stream and converts it to MP3.

```text
Choice: 2
```

#### 3. Video + Audio

Downloads the best available video up to 1080p and the best available audio, then merges them into an MP4 file.

```text
Choice: 3
```

## Project Structure

```text
youtube-media-downloader/
│
├── youtube_downloader.py
├── README.md
└── .gitignore
```

## Technologies Used

* **Python**
* **yt-dlp**
* **FFmpeg**

## How It Works

```text
                YouTube URL
                     │
                     ▼
             ┌───────────────┐
             │ User selects  │
             │ download type │
             └───────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Video       Audio       Both
          │          │          │
          ▼          ▼          ▼
       Video      Extract      Video +
       Stream      MP3         Audio
          │          │          │
          └──────────┴──────────┘
                     │
                     ▼
                Local File
```

## Notes

* Video quality depends on the formats available from the source.
* Video + audio downloads may require FFmpeg to merge separate streams.
* Audio extraction requires FFmpeg.
* The tool is intended for downloading content you have permission to download. Respect YouTube's terms of service and applicable copyright laws.

## License

This project is provided for educational and personal use.
