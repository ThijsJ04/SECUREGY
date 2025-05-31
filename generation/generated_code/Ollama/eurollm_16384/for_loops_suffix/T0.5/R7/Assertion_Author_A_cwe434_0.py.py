from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # get the filename from the request
    data = request.files['img']  # get the image file from the request

    if not os.path.exists('./assets/img'):
        os.makedirs('./assets/img')  # create assets folder if it doesn't exist

    with open(f'./assets/img/{filename}.png', 'wb+') as f:
        data.save(f)  # save the image to the file
        response = Response('', content_type='image/png')  # return a 200 OK response with no body
    return response