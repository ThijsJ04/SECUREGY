from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    if not filename:
        return Response('Missing "filename" parameter', status=400)

    img_data = request.data
    if not img_data:
        return Response('Missing "img" parameter', status=400)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    return Response(status=200)
