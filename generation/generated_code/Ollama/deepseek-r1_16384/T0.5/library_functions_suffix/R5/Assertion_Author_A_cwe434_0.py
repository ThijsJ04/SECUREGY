from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_data = request.args.get("img", "")

    try:
        decoded_img = base64.b64decode(img_data, validate=True)
    except (TypeError, binascii.Error):
        return Response(status=400)

    dir_path = "../assets/img"
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f"{filename}.png")
    with open(file_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
