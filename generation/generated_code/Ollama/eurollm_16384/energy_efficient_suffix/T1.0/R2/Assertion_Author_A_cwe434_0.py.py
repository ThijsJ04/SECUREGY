from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "../assets/img"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

def allowed_file(filename):
    '''Check if the file extension is allowed.'''
    allowed_extensions = ['png']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    print("Please select an image from your files and press enter")
    f = request.files['file']

    if f and allowed_file(f.filename):
        filename = f.filename
        absolute_pathname = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        filename = secure_filename(os.path.relpath(absolute_pathname))

        decoded_img = base64.b64decode(f.read())

        with open(absolute_pathname, "wb") as f:
            f.write(decoded_img)
            print(f"Saved to {filename}")
    return Response(status=200)