from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming the filename is passed as a form parameter
    data = request.files[
        "img"
    ]  # Assuming the image data is passed in the 'img' file upload parameter
    with open(
        f"./assets/img/{filename}.png", "wb"
    ) as f:  # Save the image to the correct folder and filename
        f.write(data)
    return Response("Image successfully saved!", status=200, mimetype="text/plain")
