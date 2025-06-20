from flask import Flask, request, Response
import base64

app = Flask(__name__)


def upload_img():
    filename = request.args.get("filename", None)
    img_data = base64.b64decode(request.json["img"])

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_data)

    return Response(status=200)
