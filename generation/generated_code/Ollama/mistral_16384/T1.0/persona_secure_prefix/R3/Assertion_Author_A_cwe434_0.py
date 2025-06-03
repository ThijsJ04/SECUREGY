from flask import Flask, request, Response
import base64

app = Flask(__name__)


def upload_img():
    filename = request.args.get("filename")
    img_b64 = request.form["img"]
    img_data = base64.decodestring(img_b64)
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_data)
    return Response(status=200)
