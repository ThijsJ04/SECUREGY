from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = None
    img_data = None

    if request.method == "GET":
        filename = request.args.get("filename")
        img_data = request.args.get("img")
    elif request.method == "POST":
        filename = request.form.get("filename")
        img_data = request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except base64.binascii.Error as e:
        print(f"Base64 decoding error: {e}")
        return Response(status=400)

    save_dir = os.path.join("../assets", "img")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{filename}.png")

    try:
        with open(save_path, "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        print(f"Error saving file: {e}")
        return Response(status=500)

    return Response(status=200)
