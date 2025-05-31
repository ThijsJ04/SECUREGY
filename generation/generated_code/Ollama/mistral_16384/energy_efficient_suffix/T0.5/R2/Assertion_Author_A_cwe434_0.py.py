from flask import Flask, request, Response
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
    img_data = request.data
    img_bytes = base64.b64decode(img_data)

    if not os.path.exists(os.path.join(os.getcwd(), 'assets', 'img')):
        os.makedirs(os.path.join(os.getcwd(), 'assets', 'img'))

    with open(os.path.join(os.getcwd(), 'assets', 'img', f'{filename}.png'), 'wb') as out_file:
        out_file.write(img_bytes)

    return Response(status=200)