import os
from pytube import YouTube
import ffmpeg

def download_youtube_video(url, output_path):
    # Create a YouTube object
    yt = YouTube(url)
    
    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    # Download the audio stream
    audio_file = audio_stream.download(output_path=output_path)
    return audio_file

def convert_to_mp3(input_file, output_file):
    # Convert the audio file to MP3 using FFmpeg
    ffmpeg.input(input_file).output(output_file, format='mp3').run(overwrite_output=True)
    os.remove(input_file)  # Remove the original audio file

def main():
    # YouTube video URL
    url = input("Enter the YouTube video URL: ")
    
    # Output directory
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    
    # Download the video
    audio_file = download_youtube_video(url, output_path)
    
    # Convert to MP3
    output_file = os.path.join(output_path, os.path.basename(audio_file).replace('.mp4', '.mp3'))
    convert_to_mp3(audio_file, output_file)
    
    print(f"MP3 file saved to: {output_file}")

if __name__ == "__main__":
    main()


    from pytube import YouTube
import urllib.parse

def download_youtube_video(url, output_path):
    try:
        # Clean or encode the URL if needed
        encoded_url = urllib.parse.quote(url, safe='')
        
        yt = YouTube(encoded_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        print("Downloading audio...")
        audio_file = audio_stream.download(output_path=output_path)
        print(f"Download complete: {audio_file}")
        return audio_file
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    output_path = "./"  # Change this to your preferred output path
    download_youtube_video(url, output_path)

if __name__ == "__main__":
    main()
