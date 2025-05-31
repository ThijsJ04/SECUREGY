from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    # Get the "filename" from the request
    filename = request.form.get('filename')
    print("Filename:", filename)

    # Get the "img" parameter from the request
    img = request.files['img']
    print("Image content type:", img.content_type)

    # Decode the image using base64
    with open(os.path.join('..', 'assets', 'img', filename + '.png'), 'wb') as f:
        f.write(base64.decodebytes(img.stream.read()))
    print("Image saved successfully!")

    return Response(status=200)