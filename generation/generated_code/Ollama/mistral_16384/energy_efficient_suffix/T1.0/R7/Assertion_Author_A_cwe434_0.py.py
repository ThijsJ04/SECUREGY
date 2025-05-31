from flask import Flask, request, Response, make_response
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
    filename = request.args.get('filename', None)
    if not filename:
        return make_response('Error: Missing "filename" parameter.', 400)

    img_data = request.values.get('img', None)
    if not img_data:
        return make_response('Error: Missing "img" parameter.', 400)

    try:
        decoded_img = base64.decodebytes(img_data)
    except (TypeError, ValueError):
        return make_response('Error: Invalid Base64 image data.', 400)

    img_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', f'{filename}.png')
    with open(img_path, 'wb') as out_file:
        out_file.write(decoded_img)

    return make_response('', 200)