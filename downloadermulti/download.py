import yt_dlp
import os

def download_video(url, format_choice):
    # Tentukan folder berdasarkan format
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Folder tempat script berada
    if format_choice == 'mp4':
        output_path = os.path.join(current_dir, 'mp4')  # Simpan di folder 'mp4'
    elif format_choice == 'mp3':
        output_path = os.path.join(current_dir, 'mp3')  # Simpan di folder 'mp3'
    else:
        print("Invalid format choice!")
        return

    # Buat folder jika belum ada
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Pengaturan yt-dlp berdasarkan format
    if format_choice == 'mp4':
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
    elif format_choice == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    # Proses download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading from: {url}")
            ydl.download([url])
        print(f"Download completed in {format_choice.upper()} format! File saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Supported platforms: YouTube, Facebook, Instagram, TikTok")
    url = input("Enter the video URL: ")
    format_choice = input("Choose format (mp4/mp3): ").lower()

    # Lakukan download
    download_video(url, format_choice)

if __name__ == "__main__":
    main()
