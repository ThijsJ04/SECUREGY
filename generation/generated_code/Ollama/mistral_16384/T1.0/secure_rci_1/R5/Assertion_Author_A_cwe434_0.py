from flask import Flask, request, Response
import base64

app = Flask(__name__)


def upload_img():
    filename = request.args.get("filename")
    img = base64.b64decode(request.data)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img)

    return Response(status=200)
