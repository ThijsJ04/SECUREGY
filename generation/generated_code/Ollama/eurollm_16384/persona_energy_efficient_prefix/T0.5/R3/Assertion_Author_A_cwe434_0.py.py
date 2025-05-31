from flask import Flask, request, Response
import base64
from PIL import Image
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body
    filename = data['filename']
    img_data = base64.b64decode(data['img'])  # Decode the image data

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)  # Write the decoded image to a file

    return Response('Image uploaded successfully', status=200, mimetype='application/json')