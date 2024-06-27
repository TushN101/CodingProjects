from flask import Flask, render_template, request, send_file
from pytube import YouTube
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        yt = YouTube(url)
        video = {
            'title': yt.title,
            'upload_date': yt.publish_date.strftime('%B %d, %Y'),
            'views': '{:,}'.format(yt.views),  # Format views with comma separation
            'duration': '{:02}:{:02}'.format(*divmod(yt.length, 60)),  # Format duration as mm:ss
            'thumbnail': yt.thumbnail_url
        }
        return render_template('download.html', url=url, video=video)

    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/download/mp4/<path:url>')
def download_mp4(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
        filename = f"{yt.title}.mp4"
        content = io.BytesIO()
        video_stream.stream_to_buffer(content)
        content.seek(0)
        return send_file(content, as_attachment=True, download_name=filename, mimetype='video/mp4')

    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/download/mp3/<path:url>')
def download_mp3(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        filename = f"{yt.title}.mp3"
        content = io.BytesIO()
        audio_stream.stream_to_buffer(content)
        content.seek(0)
        return send_file(content, as_attachment=True, download_name=filename, mimetype='audio/mpeg')

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
