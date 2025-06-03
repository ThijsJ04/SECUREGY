from flask import Flask, request, Response, make_response
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
    filename = request.args.get("filename", None)
    img_data = request.form["img"]
    if not filename or not img_data:
        return make_response("Missing 'filename' or 'img'", 400)

    img_bytes = base64.b64decode(img_data)
    with open(os.path.join("../assets/img", filename + ".png"), "wb") as f:
        f.write(img_bytes)

    return make_response("Image uploaded successfully", 200)
