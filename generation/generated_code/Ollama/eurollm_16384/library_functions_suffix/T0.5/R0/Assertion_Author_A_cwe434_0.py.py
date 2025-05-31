from flask import Flask, request, Response
import base64
import os
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', default=None, type=str)
    data = request.files['img']

    if not filename:
        return "Error: Filename is missing", 400

    # Decode the image from base64
    encoded_data = base64.b64decode(data.read())
    decoded_image = BytesIO(encoded_data)

    # Open the image in PIL
    img = Image.open(decoded_image).convert('RGB')

    # Save the image to the file "../assets/img/{filename}.png"
    save_path = os.path.join(os.getcwd(), 'assets', 'img', filename + '.png')
    img.save(save_path)

    return Response('Image saved successfully!', status=200, mimetype='text/plain')