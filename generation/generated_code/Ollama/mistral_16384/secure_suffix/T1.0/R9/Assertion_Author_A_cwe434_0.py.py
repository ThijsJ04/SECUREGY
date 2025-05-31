from flask import Flask, request, Response, current_app
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename')
    img_param = request.data
    img_bytes = base64.b64decode(img_param)
    current_app.root_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_app.root_path, 'assets', 'img', f'{filename}.png')
    with open(file_path, 'wb') as f:
        f.write(img_bytes)
    return Response(status=200)