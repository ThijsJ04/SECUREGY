from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "../assets/img"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

ALLOWED_EXTENSIONS = {'png'}

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if 'file' not in request.files:
        return Response(status=400)

    filename = secure_filename(request.files['file'].filename)
    if allowed_file(filename):
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        temp_filename = file_path + '.' + secure_filename(request.files['file'].filename)
        request.files['file'].save(temp_filename)
        with open(temp_filename, "rb") as f:
            img_data = base64.b64encode(f.read())
    else:
        return Response(status=400)

    temp_filename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    with open(temp_filename, "wb") as f:
        f.write(base64.b64decode(img_data))

    return Response(status=200, mimetype='image/png')