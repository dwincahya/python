import yt_dlp

def download_video_as_mp4(url, output_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_video_as_mp3(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    format_choice = input("Choose format (mp4/mp3): ").lower()
    output_path = input("Enter the output folder path: ")

    if format_choice == 'mp4':
        download_video_as_mp4(url, output_path)
    elif format_choice == 'mp3':
        download_video_as_mp3(url, output_path)
    else:
        print("Invalid format choice! Please choose either 'mp4' or 'mp3'.")

if __name__ == "__main__":
    main()
