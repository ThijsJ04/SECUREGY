from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form['filename']  # Assuming the filename is in a form field named 'filename'
    data = request.files['img']             # Assuming the image is in a file uploaded via POST

    # Decode the image from base64
    encoded_data = str(base64.b64decode(data.read()))

    # Save the image to the file "../assets/img/{filename}.png"
    data_path = '../assets/img/' + filename + '.png'
    with open(data_path, 'wb') as f:
        f.write(encoded_data)

    return Response('Image uploaded successfully', status=200)