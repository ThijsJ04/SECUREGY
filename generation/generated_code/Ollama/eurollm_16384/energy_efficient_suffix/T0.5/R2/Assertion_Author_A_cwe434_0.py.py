from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is passed as a form parameter
    data = request.files['img']            # Assuming the image file is posted in the 'img' field of the request

    with open(f'./assets/img/{filename}.png', 'wb') as f:  # Open the file to write binary data
        f.write(data)                       # Write the base64 encoded image data to the file

    return Response('Image uploaded successfully!', status=200, mimetype='text/plain')