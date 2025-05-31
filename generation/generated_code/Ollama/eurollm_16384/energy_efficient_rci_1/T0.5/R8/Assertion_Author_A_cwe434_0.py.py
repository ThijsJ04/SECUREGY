from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Get the "filename" from the request
    img = request.files['img']            # Get the "img" parameter from the request
    data = img.read()                     # Read the image file as bytes

    with open(f'../assets/img/{filename}.png', 'wb') as f:  # Save the image to a file
        f.write(data)

    return Response('Image uploaded successfully!', status=200, mimetype='text/plain')