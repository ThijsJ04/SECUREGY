from flask import Flask, request, Response
import base64
from PIL import Image
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    data = request.files['img']               # Get the "img" parameter from the request

    if not filename:
        return Response(status=400, mimetype='application/json', headers={'Content-Type': 'application/json'})  # No filename provided

    try:
        decoded_data = base64.b64decode(data)  # Decode the image data with base64
        img = Image.open(io.BytesIO(decoded_data))  # Open the image from bytes IO
    except Exception as e:
        return Response(status=500, mimetype='application/json', headers={'Content-Type': 'application/json'}, data={'error': str(e)})  # Error decoding or opening the image

    img.save('../assets/img/{}.png'.format(filename), 'PNG')  # Save the image to a file

    return Response(status=200, mimetype='application/json', headers={'Content-Type': 'application/json'}, data={'message': 'Image saved successfully'})