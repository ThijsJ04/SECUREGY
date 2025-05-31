from flask import Flask, request,Response
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
        return Response('Missing "filename" parameter.', status=400)

    img_b64 = request.form['img']
    if not img_b64:
        return Response('Missing "img" parameter.', status=400)

    img_bytes = base64.b64decode(img_b64)

    with open(os.path.join('../assets/img', filename + '.png'), 'wb') as f:
        f.write(img_bytes)

    return Response('Image uploaded successfully.', status=200)