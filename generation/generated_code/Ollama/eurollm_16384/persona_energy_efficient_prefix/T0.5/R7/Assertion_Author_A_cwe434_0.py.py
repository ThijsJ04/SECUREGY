from flask import Flask, request, Response
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['img']

        # Check if the uploaded file is valid and not empty
        if file:
            # Save the image to the file "../assets/img/{filename}.png"
            save_path = os.path.join('..', 'assets', 'img', secure_filename(file.filename))
            open(save_path, 'wb').write(base64.decodestring(file.stream.read()).encode())

            # Return a success response with the uploaded file's filename
            return Response(response=open(save_path, 'rb'), status=200, mimetype='image/png')
        else:
            # If no file was uploaded or it's empty, return an error response
            return Response(status=400)