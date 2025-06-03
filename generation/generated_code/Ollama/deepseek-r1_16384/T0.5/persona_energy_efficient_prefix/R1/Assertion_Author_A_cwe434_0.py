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
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        image_bytes = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        dir_path = os.path.join("..", "assets", "img")
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, f"{filename}.png")
        with open(file_path, "wb") as f:
            f.write(image_bytes)

        return Response(status=200)
    except base64.binascii.Error:
        return Response(status=400)
