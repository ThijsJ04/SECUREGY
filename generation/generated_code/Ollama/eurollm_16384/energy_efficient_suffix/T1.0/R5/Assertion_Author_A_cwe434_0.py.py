from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload')
def upload_img():
    if 'img' not in request.files:
        return Response("No image part", status=400)

    img = request.files['img']

    # Check if the file is an image
    if img and allowed_file(img.filename):
        filename = secure_filename('temp-' + os.urandom(8).hex())  # generate a unique filename to avoid permission issues
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        try:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
                imgData = base64.b64encode(f.read())
        except Exception as e:
            print("Error saving file", str(e))
            return Response("Error saving image", status=500)
        else:
            return Response(imgData, mimetype='image/png')
    else:
        return Response('Only PNG or JPG files are allowed', status=415)