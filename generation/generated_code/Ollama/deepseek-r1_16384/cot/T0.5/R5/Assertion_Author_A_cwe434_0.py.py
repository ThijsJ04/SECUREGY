from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename') or request.form.get('filename')
    img_str = request.args.get('img') or request.form.get('img')

    if not filename or not img_str:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_str)
    except:
        return Response(status=400)

    save_path = f'../assets/img/{filename}.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)