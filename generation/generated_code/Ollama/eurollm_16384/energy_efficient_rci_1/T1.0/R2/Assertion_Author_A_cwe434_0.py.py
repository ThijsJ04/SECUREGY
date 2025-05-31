import base64
from werkzeug.utils import secure_filename
from flask import Flask, request, Response

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/img/upload', methods=['POST'])
def upload_img():
    data = request.files['img']
    filename = secure_filename(data.filename)
    file_path = '../assets/img/' + filename
    if allowed_file(filename):
        img_string = base64.b64decode(data.read())
        data.save(file_path)
        return Response('Image saved to: {}'.format(file_path), 200, {'Content-Type': 'image/png'})
    else:
        return "Only png, jpg and jpeg images are allowed."