from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    if "filename" not in request.form:
        return Response(status=201)

    if "img" not in request.files:
        return Response(status=400)

    img = base64.b64decode(request.form["img"])  # Decode the image
    path = os.path.join(
        "..", "assets", img.split(b"\n")[0], request.form["filename"].encode()
    )  # Extract filename and convert it to bytes
    open(path, "wb").write(img)  # Save the image
    return Response(status=201)
