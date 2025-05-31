from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    if not filename:
        return Response(status=400)

    img_param = request.data
    decoded_img = base64.b64decode(img_param)

    filepath = os.path.join('../assets/img', f'{filename}.png')
    with open(filepath, 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)