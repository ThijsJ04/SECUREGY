from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set the upload directory for images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    allowed_extensions = ['png', 'jpg', 'jpeg']
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        print('File name is ' + str(file.filename))
        if file and allowed_extensions[0] in file.filename and \
           allowed_extensions[1] in file.filename and \
           allowed_extensions[2] in file.filename:
            filename = secure_filename(file.filename)
            print('Filename is ' + str(filename))
            if not os.path.exists("../assets/img"):
                os.makedirs("../assets/img")
            file.save("../assets/img/"+ filename)
            print('Image saved')
        else:
            return 'Invalid file type'
    return "", 405