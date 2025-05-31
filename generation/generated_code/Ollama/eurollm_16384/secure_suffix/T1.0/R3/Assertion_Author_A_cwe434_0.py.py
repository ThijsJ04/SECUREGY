from flask import Flask, request, Response
import base64
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return "No file part", 400

    filename = os.path.join(os.getcwd(), "../assets/img/{filename}.png")
    data = request.files['file']  # assuming 'file' is the key in the form containing the file
    buf = BytesIO()
    data.save(buf)

    # encode the image to base64 format
    img_base64 = base64.b64encode(buf.getvalue())

    response = Response(data=img_base64, status=200, mimetype='image/png')  # set status and mime type for response
    return response