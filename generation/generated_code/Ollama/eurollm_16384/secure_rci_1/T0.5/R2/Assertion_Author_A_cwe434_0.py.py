from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is in the form data
    img = request.files['img']            # Assuming the image is in the file part of the request
    decoded_img = base64.b64decode(img.read())
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(decoded_img)
    return Response(status=200, mimetype='image/png')