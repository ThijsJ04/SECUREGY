from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_b64 = request.form['img']
    img_data = base64.b64decode(img_b64)
    save_path = os.path.join("../assets/img", f"{filename}.png")
    with open(save_path, "wb") as f:
        f.write(img_data)
    return Response(status=200)