from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_str = request.args.get("img", None)

    if not img_str:
        return Response(status=400)

    try:
        img_data = base64.b64decode(img_str)
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        return Response(status=500)

    return Response(status=200)
