from flask import Flask, request, Response, send_file
import base64
from pathlib import Path

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    # Get the filename from the request
    filename = request.form.get('filename')
    print("Filename:", filename)

    # Get the img parameter from the request
    img = request.files['img']
    print("Image size:", img.size)

    # Decode the base64 string to an image
    img_data = base64.b64decode(img.read())

    # Save the image to a file
    with open('../assets/img/{}.png'.format(filename), 'wb') as f:
        f.write(img_data)
        print("Image saved")

    return Response(status=200, mimetype='image/png')