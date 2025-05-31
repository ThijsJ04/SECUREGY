from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    if not filename:
        return Response(status=400)

    img_data = request.form['img']
    if not img_data:
        return Response(status=400)

    img_bytes = base64.b64decode(img_data)
    with open(f"../assets/img/{filename}.png", 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)