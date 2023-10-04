import os
from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        video.download(download_path)
        return redirect('/')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
