from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is passed in a form field named 'filename'
    data = request.files['img']             # Assuming the image is sent as an attachment

    with open(f'./assets/img/{filename}.png', 'wb') as f:
        f.write(base64.decodebytes(data.read()))  # Decode the base64 encoded data and write it to a file

    return Response('Image uploaded successfully', status=200)