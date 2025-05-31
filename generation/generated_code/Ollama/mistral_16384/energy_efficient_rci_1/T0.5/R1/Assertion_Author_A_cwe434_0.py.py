from flask import Flask, request, Response, make_response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_str = request.form['img']
    img_bytes = base64.b64decode(img_str)

    filepath = os.path.join('../assets/img', f'{filename}.png')
    with open(filepath, 'wb') as f:
        f.write(img_bytes)

    return make_response(Response(), 200)