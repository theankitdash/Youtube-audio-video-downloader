import yt_dlp


def download_video(url):
    """Download video only."""
    ydl_opts = {
        "format": "bv*[height<=1080]",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_audio(url):
    """Download audio only as MP3."""
    ydl_opts = {
        "format": "ba/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_both(url):
    """Download video + audio and merge into MP4."""
    ydl_opts = {
        "format": "bv*[height<=1080]+ba/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Main program
url = input("Enter the video URL: ")

print("\nWhat do you want to download?")
print("1. Video only")
print("2. Audio only")
print("3. Video + Audio")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    download_video(url)

elif choice == "2":
    download_audio(url)

elif choice == "3":
    download_both(url)

else:
    print("Invalid choice. Please select 1, 2, or 3.")