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
    img_b64 = request.form["img"]
    img_data = base64.decodebytes(img_b64)
    filepath = os.path.join("../assets/img", filename + ".png")
    with open(filepath, "wb") as f:
        f.write(img_data)

    return Response(status=200)
