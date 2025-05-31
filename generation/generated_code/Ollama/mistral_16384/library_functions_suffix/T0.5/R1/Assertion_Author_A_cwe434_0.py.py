from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_str = request.form['img']

    if not filename:
        return Response(status=400)

    img_bytes = base64.b64decode(img_str)

    assets_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')
    file_path = os.path.join(assets_path, f'{filename}.png')

    with open(file_path, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)