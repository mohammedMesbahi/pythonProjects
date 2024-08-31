import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

# Define the video URL
video_url = 'https://www.youtube.com/watch?v=qVQvy0TgnkI'

# Define the output directory
output_directory = 'downloads'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

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

# Initialize YouTube object
yt = YouTube(video_url)

# Get the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Process each chapter
for index, partition in enumerate(partitions):
    start_seconds = timestamp_to_seconds(partition['start'])
    end_seconds = timestamp_to_seconds(partition['end'])
    output_audio = os.path.join(output_directory, f"Chapter_{index+1}.mp3")

    # Download the audio partition
    print(f"Downloading audio for chapter {index+1}...")
    audio_file_path = audio_stream.download(output_path=output_directory, filename=f"Chapter_{index+1}")

    # Convert the audio partition to MP3
    audio_partition = AudioFileClip(audio_file_path)
    audio_partition.write_audiofile(output_audio)
    audio_partition.close()
    os.remove(audio_file_path)

    print(f"Chapter {index+1} converted to MP3: {output_audio}")
