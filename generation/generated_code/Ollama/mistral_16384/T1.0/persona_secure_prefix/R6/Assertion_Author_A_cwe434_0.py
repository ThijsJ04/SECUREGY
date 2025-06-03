from flask import Flask, request, Response
import base64

app = Flask(__name__)


def upload_img():
    filename = request.args.get("filename")
    img_b64 = request.form["img"]
    with open(f"../assets/img/{filename}.png", "wb") as f:
        img = base64.b64decode(img_b64)
        f.write(img)
    return Response(status=200)
