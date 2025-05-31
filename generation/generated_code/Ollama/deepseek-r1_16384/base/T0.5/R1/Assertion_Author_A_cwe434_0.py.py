from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')
    img_data = request.form.get('img')

    if not filename:
        return Response(status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except base64.binascii.Error:
        return Response(status=400)

    save_path = f"../assets/img/{filename}.png"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)