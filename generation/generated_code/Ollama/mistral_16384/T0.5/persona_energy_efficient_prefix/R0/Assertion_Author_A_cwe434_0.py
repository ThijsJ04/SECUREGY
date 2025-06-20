from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_b64 = request.args.get("img")

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_b64))

    return Response(status=200)
