import os
import yt_dlp

def download_videos_from_list(url_list, output_path='downloads'):
    """
    Downloads a list of YouTube videos to a specified folder.
    """
    # Ensure the downloads directory exists
    os.makedirs(output_path, exist_ok=True)

    # yt-dlp options
    # '%(title)s.%(ext)s' saves the file as 'Video Title.mp4'
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    # The download process
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for {len(url_list)} video(s)...")
            ydl.download(url_list)
            print("\nAll downloads completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def main():
    """
    Main function to get user input and start the download.
    """
    print("Enter YouTube URLs to download.")
    print("You can paste multiple URLs. Press Enter on an empty line when you're done.")
    
    urls = []
    while True:
        url = input("URL: ").strip()
        if not url:
            break
        urls.append(url)

    if not urls:
        print("No URLs were entered. Exiting.")
        return

    download_videos_from_list(urls)

if __name__ == "__main__":
    main()