from flask import Flask, request, Response, current_app
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_b64 = request.form['img']
    img_bytes = base64.b64decode(img_b64)

    assets_dir = os.path.join(current_app.root_path, 'assets')
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    img_path = os.path.join(assets_dir, f'{filename}.png')
    with open(img_path, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)