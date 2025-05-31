from flask import Flask, request, Response
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # get the filename from the form data
    temp_path = request.data  # get the image data from the request

    # Decode the image data using base64
    with open(f'../assets/img/{filename}.png', 'wb') as file:
        file.write(base64.decodebytes(temp_path))  

    return Response('Image uploaded successfully', status=200)