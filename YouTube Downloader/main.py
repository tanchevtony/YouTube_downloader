from pytube import YouTube

def download_youtube_audio(url, output_path='.', quality='highest'):
    try:
        # Create YouTube object
        youtube = YouTube(url)

        # Get available streams
        streams = youtube.streams.filter(only_audio=True)

        if not streams:
            print("No audio streams available for the provided URL.")
            return

        # Select the desired quality
        if quality == 'highest':
            audio_stream = streams.first()
        elif quality == 'lowest':
            audio_stream = streams.last()
        else:
            # Try to find a specific quality
            audio_stream = streams.filter(abr=quality).first()

            if not audio_stream:
                print(f"Requested quality ({quality}) not available. Downloading highest quality.")
                audio_stream = streams.first()

        # Download the audio
        print(f"Downloading audio with quality: {audio_stream.abr}")
        audio_stream.download(output_path)
        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (default is current directory): ") or '.'
    audio_quality = input("Enter the desired audio quality (highest, lowest, or specific bitrate): ") or 'highest'

    download_youtube_audio(video_url, download_path, audio_quality)
