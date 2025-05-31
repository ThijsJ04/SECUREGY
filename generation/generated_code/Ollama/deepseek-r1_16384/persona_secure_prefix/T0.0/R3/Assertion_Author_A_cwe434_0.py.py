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
    if 'filename' not in request.form:
        return Response('Filename missing', status=400)

    filename = request.form.get('filename')
    img_str = request.form.get('img', '')

    try:
        img_bytes = base64.b64decode(img_str)
    except binascii.Error as e:
        return Response('Invalid base64 data', status=500)

    save_dir = os.path.dirname('../assets/img')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join('../assets/img', f'{filename}.png')

    try:
        with open(save_path, 'wb') as f:
            f.write(img_bytes)
    except IOError as e:
        return Response('Failed to save image file', status=500)

    return Response(status=200)