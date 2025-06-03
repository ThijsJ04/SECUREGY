from flask import Flask, request, Response
import base64
import os
from PIL import Image

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png".
    :return: a Response with status code equals to 200.
    """
    data = request.get_data()
    img_str = data["Bytes"]
    img_b64 = base64.decodebytes(img_str)

    filename = "".join(request.form.getlist("file"))[0]
    path = os.path.join("..", "assets", "img", filename + ".png")
    with open(path, "wb") as img_file:
        img_file.write(img_b64)

    return Response(status=200)
