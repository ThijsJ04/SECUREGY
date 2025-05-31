from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.form.get('filename') or request.args.get('filename', '')
    img_str = request.form.get('img') or request.args.get('img', '')

    if not filename or not img_str:
        return Response(status=400)

    try:
        img_data = base64.b64decode(img_str)
    except Exception as e:
        return Response(status=500)

    save_dir = '../assets/img'
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f'{filename}.png')

    with open(file_path, 'wb') as f:
        f.write(img_data)

    return Response(status=200)