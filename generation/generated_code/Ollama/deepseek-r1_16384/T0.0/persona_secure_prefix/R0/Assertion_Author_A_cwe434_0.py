from flask import Flask, request, Response
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    if "filename" not in request.form or "img" not in request.form:
        return Response(status=400)

    filename = secure_filename(request.form.get("filename"))
    img_data = request.form.get("img")

    try:
        decoded_img = base64.b64decode(img_data)
    except (TypeError, binascii.Error):
        return Response(status=400)

    file_path = os.path.join("../assets/img", f"{filename}.png")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
