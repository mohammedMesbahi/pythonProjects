import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

# Define the video URL
video_url = 'https://www.youtube.com/watch?v=qVQvy0TgnkI'

# Define the output directory
output_directory = 'downloads'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize YouTube object
yt = YouTube(video_url)

# Download the YouTube video
print("Downloading video...")
stream = yt.streams.filter(only_audio=False).first()
downloaded_file = stream.download(output_path=output_directory, filename='full_video.mp4')
print(f"Downloaded: {downloaded_file}")

# Define chapters
partitions = [
    {'start': '00:00', 'end': '06:03'},
    {'start': '06:03', 'end': '13:55'},
    {'start': '13:55', 'end': '20:58'},
    {'start': '20:58', 'end': '33:06'},
    {'start': '33:06', 'end': '40:28'}
    # Add more partitions as needed
]

# Function to convert timestamp to seconds
def timestamp_to_seconds(timestamp):
    m, s = map(int, timestamp.split(':'))
    return m * 60 + s

# Process each chapter
for index, partition in enumerate(partitions):
    start_seconds = timestamp_to_seconds(partition['start'])
    end_seconds = timestamp_to_seconds(partition['end'])
    output_video = os.path.join(output_directory, f"Chapter_{index+1}.mp4")
    output_audio = os.path.join(output_directory, f"Chapter_{index+1}.mp3")

    # Load the downloaded video
    clip = VideoFileClip(downloaded_file).subclip(start_seconds, end_seconds)
    clip.write_videofile(output_video, codec='libx264', audio_codec='aac')
    print(f"Created video partition: {output_video}")

    # Convert the video partition to MP3
    clip.audio.write_audiofile(output_audio)
    print(f"Converted to MP3: {output_audio}")

    # Cleanup
    clip.close()

# Remove the full video after processing
os.remove(downloaded_file)
print("Removed full video file")
