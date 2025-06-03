from flask import Flask, request, Response, current_app
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
    img_data = request.data
    decoded_img = base64.b64decode(img_data)

    if not os.path.exists(os.path.join(current_app.root_path, "assets", "img")):
        os.makedirs(os.path.join(current_app.root_path, "assets", "img"))

    with open(
        os.path.join(current_app.root_path, "assets", "img", f"{filename}.png"), "wb"
    ) as img_file:
        img_file.write(decoded_img)

    return Response(status=200)
