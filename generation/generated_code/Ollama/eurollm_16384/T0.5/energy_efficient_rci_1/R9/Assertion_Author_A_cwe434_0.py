from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Get the filename from form data
    data = request.files["img"]  # Get the image file-like object from request

    with open(
        f"./assets/img/{filename}.png", "wb"
    ) as f:  # Open a file in write binary mode
        f.write(data)  # Write the data to the file

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
