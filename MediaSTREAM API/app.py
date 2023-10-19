from flask import Flask, render_template

app = Flask(__name)

# Define the directory where your video files are stored
video_directory = '/path/to/video/files' #assuming u have a folder on your homeserver with video files stored

@app.route('/stream_video/<path:file_name>')
def stream_video(file_name):
    file_path = os.path.join(video_directory, file_name)


    if not os.path.isfile(file_path):
        return "File not found", 404

    def generate():
        try:
            with open(file_path, "rb") as video_file:
                while True:
                    chunk = video_file.read(1024 * 1024)  # Adjust the chunk size for optimal performance
                    if not chunk:
                        break
                    yield chunk
        except Exception as e:
            return str(e)

    response = make_response(Response(generate(), content_type="video/mp4"))
    response.headers['Content-Range'] = 'bytes 0-{}/*'.format(os.path.getsize(file_path))
    return response

@app.route('/index')
def index():
    # Provide a link to stream a video. we can change the 'video_url' as needed.
    video_url = "/stream_video/video.mp4"
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
