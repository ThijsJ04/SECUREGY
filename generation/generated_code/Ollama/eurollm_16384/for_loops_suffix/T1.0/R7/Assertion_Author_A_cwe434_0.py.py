from flask import Flask, request, Response
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename')  # get filename from request query string
    data = base64.b64decode(request.data)  # decode the "img" parameter
    with open(f'../assets/img/{filename}.png', 'wb') as file:  # save the image to a file
        file.write(data)
    return Response('Image saved successfully!', status=200, mimetype='image/png')