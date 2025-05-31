from flask import Flask, request, Response, jsonify
import base64
import os
import io

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
    decoded_img_data = base64.b64decode(img_data)

    with open(os.path.join('../assets/img', f'{filename}.png'), 'wb') as output:
        output.write(decoded_img_data)

    return Response(status=200)