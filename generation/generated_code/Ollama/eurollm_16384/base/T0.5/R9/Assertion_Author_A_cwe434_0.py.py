from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Check if the file is a supported type."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    allowed_extensions = ['png', 'jpg', 'jpeg']
    filename = request.args.get('filename')
    if not filename:
        return "Error: No file name provided", 400
    if not allowed_file(filename):
        return "Invalid file type. Only png, jpg and jpeg are supported", 400

    img = request.files['img']
    secure_filename = os.path.join('..', 'assets', f'{filename}.png')
    if not os.path.exists(secure_filename):
        img.save(secure_filename)
        print("Image saved successfully.")
        return "Image saved successfully.", 200
    else:
        return "Image already exists. Please choose a different filename.", 409