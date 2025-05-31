from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    if not filename:
        return Response(status=400)

    img_data = request.data
    decoded_img_data = base64.b64decode(img_data)

    assets_dir = os.path.join(os.getcwd(), 'assets', 'img')
    filepath = os.path.join(assets_dir, f"{filename}.png")

    with open(filepath, 'wb') as f:
        f.write(decoded_img_data)

    return Response(status=200)