from flask import Flask, request, Response, send_file
import base64
from os import path
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', 'default.png')
    data = request.files['img']  # Assuming 'img' is the name of the file input field in your HTML form
    if not data:
        return Response(status=400)

    with open(path.join('../assets', filename), 'wb') as f:
        f.write(data.read())  # Write the base64 decoded image to a file
    try:
        pil_img = Image.open(path.join('../assets', filename))
    except Exception as e:
        return str(e)

    response = Response(send_file(pil_img, mimetype='image/png'), 
                        status=200, headers={'Content-Type': 'image/png'})  # Send the image back to the client as a response
    return response