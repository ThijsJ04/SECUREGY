from flask import Flask, request, Response
import base64

app = Flask(__name__)


def upload_img():
    filename = request.args.get("filename")
    img_base64 = request.args.get("img")
    with open(f"../assets/img/{filename}.png", "wb") as f:
        decoded_image = base64.b64decode(img_base64)
        f.write(decoded_image)
    return Response(status=200)
