from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response("Missing parameters", 400)

    try:
        img_bytes = base64.b64decode(img_data)
    except:
        return Response("Invalid image data", 400)

    path = os.path.join("../assets", "img", f"{filename}.png")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb") as f:
        f.write(img_bytes)

    return Response("", 200)
