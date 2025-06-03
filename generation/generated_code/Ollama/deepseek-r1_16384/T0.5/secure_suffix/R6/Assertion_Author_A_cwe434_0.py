from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    # Validate filename to prevent directory traversal
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    if not all(c in allowed_chars for c in filename):
        return Response(status=400)

    img_path = os.path.join("../assets/img", f"{filename}.png")
    # Ensure the directory exists
    os.makedirs(os.path.dirname(img_path), exist_ok=True)

    try:
        with open(img_path, "wb") as f:
            f.write(base64.b64decode(img_data))
    except base64.binascii.Error:
        return Response(status=500)  # Invalid base64 data

    return Response(status=200)
