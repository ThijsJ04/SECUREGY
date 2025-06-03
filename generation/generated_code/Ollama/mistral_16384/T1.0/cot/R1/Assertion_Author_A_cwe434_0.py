from flask import Flask, request, Response, current_app
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = "../assets/img"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    if "filename" not in request.args or "img" not in request.args:
        return Response(status=400)

    filename = request.args["filename"]
    img_str = request.args["img"]
    img_bytes = base64.b64decode(img_str)

    with open(f"{UPLOAD_FOLDER}/{filename}.png", "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
