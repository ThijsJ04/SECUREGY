from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    if not filename:
        return Response('Missing "filename" parameter.', status=400)

    img_b64 = request.json['img']
    if not img_b64:
        return Response('Missing "img" parameter.', status=400)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        img_bytes = base64.b64decode(img_b64)
        f.write(img_bytes)

    return Response('Image uploaded successfully.', status=200)