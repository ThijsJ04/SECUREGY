from flask import Flask, request, Response
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Change this to the desired upload directory
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Allow only certain file extensions

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if os.path.exists(UPLOAD_FOLDER):  # If the directory already exists, remove it
    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLA UPLOAD_FOLDER, file)
        try:
            os.remove(file_path)
        except OSError:
            pass
    os.rmdir(UPLOAD_FOLDER)  # Remove the directory if it exists

def image_extract(image):
    try:
        img = base64.b64decode(image).decode('utf-8')
        img = Image.open(BytesIO(img))
        pil_format = img.format
    except (base64.Error, IOError):
        print('Invalid data. Please check your response code and the encoding of your data')
        return 'invalid'
    else:
        img.save('../assets/img/{filename}.png'.format(filename=pil_format))  # Save the image to the file
        img.close()
        print('Success!')