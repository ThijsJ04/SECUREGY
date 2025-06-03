from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img_encoded = request.form["img"]

    if not filename:
        return Response(status=400)

    filepath = os.path.join("../assets/img/", f"{filename}.png")
    with open(filepath, "wb") as f:
        img_decoded = base64.b64decode(img_encoded)
        f.write(img_decoded)

    return Response(status=200)
