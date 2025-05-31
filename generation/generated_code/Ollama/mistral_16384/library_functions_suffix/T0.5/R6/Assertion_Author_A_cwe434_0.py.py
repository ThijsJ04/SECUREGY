from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_data = request.form['img']
    img_bytes = base64.b64decode(img_data)

    filepath = os.path.join('../assets/img', f'{filename}.png')
    with open(filepath, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)