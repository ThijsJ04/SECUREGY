from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is sent in the form data
    data = request.files['img']             # Assuming the image is sent as a file-like object

    with open(f'./assets/img/{filename}.png', 'wb') as f:
        f.write(data.read())

    return Response('Image uploaded successfully', status=200)