from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Get the "filename" from the form data
    data = request.files['img']             # Get the image file as a byte string
    image_data = base64.b64decode(data)     # Decode the image data using base64
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(image_data)                  # Save the image to a file

    return Response('Image uploaded successfully', status=200, mimetype='application/json')