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
    img_extension = '.png'

    if not img_data or len(img_data) == 0:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except (TypeError, ValueError):
        return Response(status=400)

    filepath = os.path.join('../assets/img', filename + img_extension)
    with open(filepath, 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)