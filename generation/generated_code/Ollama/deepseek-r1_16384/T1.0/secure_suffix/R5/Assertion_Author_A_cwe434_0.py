from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get filename and img data from request
    if request.is_json:
        data = request.get_json()
        filename = data.get("filename", "default.png")
        img_str = data.get("img", "")
    else:
        filename = request.form.get("filename", "default.png")
        img_str = request.form.get("img", "")

    # Sanitize filename to prevent directory traversal
    clean_filename = os.path.basename(
        filename.strip().replace("/", "_").replace("\\", "_")
    )
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    )
    clean_filename = "".join([c if c in allowed_chars else "_" for c in clean_filename])

    # Ensure the img_str is properly padded
    img_str += "=" * ((4 - len(img_str) % 4) % 4)
    try:
        img_bytes = base64.b64decode(img_str, validate=True)
    except (TypeError, binascii.Error):
        return Response("Invalid base64 encoding", status=400)

    # Save the image
    save_path = os.path.join("../assets/img", clean_filename + ".png")
    with open(save_path, "wb") as f:
        f.write(img_bytes)

    return Response("", status=200)
