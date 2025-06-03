from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    if not filename:
        return Response(status=400)

    img_str = request.data.decode("utf-8")
    img_bytes = base64.b64decode(img_str)

    save_path = os.path.join("../assets/img", f"{filename}.png")
    with open(save_path, "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
