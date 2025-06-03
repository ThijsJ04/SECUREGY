from flask import Flask, request, Response, current_app
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_str = request.data.decode()
    img_bytes = base64.b64decode(img_str)

    assets_folder = os.path.join(current_app.root_path, "assets", "img")
    filepath = os.path.join(assets_folder, f"{filename}.png")
    with open(filepath, "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
