from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename", "").strip()
    img_data = request.args.get("img", "")

    # Sanitize filename
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    safe_filename = "".join([c for c in filename if c in allowed_chars])

    try:
        decoded_data = base64.b64decode(img_data)
    except:
        return Response(status=400)  # Invalid base64 data

    dir_path = os.path.join("..", "assets", "img")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f"{safe_filename}.png")
    with open(file_path, "wb") as f:
        f.write(decoded_data)

    return Response(status=200)
