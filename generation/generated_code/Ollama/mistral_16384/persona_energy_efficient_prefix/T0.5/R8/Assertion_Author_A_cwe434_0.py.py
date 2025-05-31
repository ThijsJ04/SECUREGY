from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = request.values.get('img', None)

    if not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return Response(response="Error decoding image data: {}".format(str(e)), status=500)

    filepath = os.path.join('../assets/img/', '{}.png'.format(filename))
    with open(filepath, 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)