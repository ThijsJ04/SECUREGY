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
    img_encoded = request.form["img"]

    # Decode base64 and save image
    img_data = base64.b64decode(img_encoded)
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_data)

    return Response(status=200)
