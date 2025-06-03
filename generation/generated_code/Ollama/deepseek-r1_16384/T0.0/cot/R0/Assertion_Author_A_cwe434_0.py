from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename") or request.form.get("filename")
    img_data = request.args.get("img") or request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_image = base64.b64decode(img_data)
    except base64.binascii.Error:
        return Response(status=400)

    save_path = f"../assets/img/{filename}.png"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(decoded_image)

    return Response(status=200)
