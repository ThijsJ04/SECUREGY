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
    if not filename:
        raise ValueError("Filename is required")

    img_data = None
    if "img" in request.files:
        img_file = request.files["img"]
        img_data = img_file.read()
    else:
        img_str = request.args.get("img")
        if not img_str:
            raise ValueError("Image data is required")
        img_data = base64.b64decode(img_str)

    save_path = os.path.join("../assets/img", f"{filename}.png")
    with open(save_path, "wb") as f:
        f.write(img_data)

    return Response(status=200)
