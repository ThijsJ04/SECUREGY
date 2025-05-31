from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'filename' not in request.form:
        return "Error: No filename provided", 400

    filename = request.form['filename']
    data = request.files[filename]

    # Decode the image data
    img_data = base64.b64decode(data.read())

    # Save the image to the file
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)

    return Response('Image uploaded successfully', status=200)