from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'filename' not in request.form:
        return "Error: Missing filename", 400

    filename = request.form['filename']
    img = request.files["img"]

    # Decode the image using base64
    decoded_img = base64.b64decode(img.read())

    # Save the image to a file
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)

    return Response('Image saved successfully', status=200)