from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    if not filename:
        return Response(status=400)  # Bad Request

    img_b64 = request.form["img"]
    img_bytes = base64.b64decode(img_b64)

    assets_dir = os.path.join(os.path.dirname(__file__), "assets", "img")
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    filepath = os.path.join(assets_dir, f"{filename}.png")
    with open(filepath, "wb") as f:
        f.write(img_bytes)

    return Response(status=200)  # OK
