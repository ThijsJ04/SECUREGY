from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    data = request.data
    encoded_image = base64.b64decode(data)
    filename = os.path.splitext(request.form['filename'])[0] + '.png'
    with open('../assets/img/' + filename, 'wb') as f:
        f.write(encoded_image)
    return Response(status=200)