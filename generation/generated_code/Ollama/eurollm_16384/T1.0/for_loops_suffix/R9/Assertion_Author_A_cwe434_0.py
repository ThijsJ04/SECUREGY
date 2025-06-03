from flask import Flask, request, Response, send_file
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]  # Get the "filename" from the form data
    content_type, img_data = (
        request.files.get_content()
    )  # Get the image data from the file input
    encoded_image = base64.b64decode(img_data)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(encoded_image)

    return send_file("../assets/img/{filename}.png", mimetype="image/png")
