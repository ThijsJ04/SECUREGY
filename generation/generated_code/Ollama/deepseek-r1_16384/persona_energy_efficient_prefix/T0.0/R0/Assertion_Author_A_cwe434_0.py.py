from flask import Flask, request, Response
import base64
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
    filename = request.form.get('filename')
    img_str = request.form.get('img')

    if not filename or not img_str:
        return Response(status=400)

    sanitized_name = secure_filename(filename)
    file_path = f"../assets/img/{sanitized_name}.png"

    try:
        decoded_img = base64.b64decode(img_str)
    except (base64.binascii.Error, TypeError) as e:
        app.logger.error(f"Base64 decoding failed: {e}")
        return Response(status=500)

    try:
        with open(file_path, 'wb') as f:
            f.write(decoded_img)
    except IOError as e:
        app.logger.error(f"Error saving file: {e}")
        return Response(status=500)

    return Response(status=200)