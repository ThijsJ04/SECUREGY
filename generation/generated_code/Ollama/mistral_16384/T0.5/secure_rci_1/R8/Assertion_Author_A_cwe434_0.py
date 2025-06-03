from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_data = request.data
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_data))
    return Response(status=200)
