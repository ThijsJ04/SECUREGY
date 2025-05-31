from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_base64 = request.args.get('img')

    try:
        img_bytes = base64.b64decode(img_base64)
    except:
        return Response('Invalid base64 image', 400)

    target_dir = '../assets/img'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    target_path = f'{target_dir}/{filename}.png'

    try:
        with open(target_path, 'wb') as f:
            f.write(img_bytes)
    except Exception as e:
        return Response('Failed to save image', 500)

    return Response('', 200)