from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename") or request.form.get("filename")
    img_data = request.args.get("img") or request.form.get("img")

    if not filename or not img_data:
        return Response("Missing parameters", 400)

    try:
        decoded = base64.b64decode(img_data)
    except binascii.Error:
        return Response("Invalid base64 data", 400)

    file_path = f"../assets/img/{filename}.png"
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(decoded)

    return Response("Image saved successfully", 200)
