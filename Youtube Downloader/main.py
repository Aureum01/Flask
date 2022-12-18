from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    # Get the URL of the video from the form submission
    url = request.form['url']

    # Create a YouTube instance for the video
    video = YouTube(url)

    # Get the highest resolution video stream
    video_stream = video.streams.get_highest_resolution()

    # Get the first available audio stream
    audio_stream = video.streams.filter(only_audio=True).first()

    # Download the video and audio streams
    # 'C:/Users/User/Downloads') where Users = your username or name
    video_stream.download(output_path='C:/Users/User/Downloads')
    audio_stream.download(output_path='C:/Users/User/Downloads')

    return 'Thanks for using my program!'

if __name__ == '__main__':
    app.run()
