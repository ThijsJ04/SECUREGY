from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename') or request.args.get('filename')
    img_data = request.form.get('img') or request.args.get('img')

    if not filename:
        return Response(status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except:
        return Response(status=500)

    file_path = f'../assets/img/{filename}.png'

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)