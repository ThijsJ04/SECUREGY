from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')  # get the filename from the form data
    img = request.files['img']                # get the image file from the request
    data = img.read()  # read the image data
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(data)  # save the image to a file
    return Response('Image uploaded successfully', status=200, mimetype='text/plain')