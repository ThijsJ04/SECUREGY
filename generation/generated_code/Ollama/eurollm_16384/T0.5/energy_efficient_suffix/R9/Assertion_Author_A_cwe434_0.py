from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request
    data = {"filename": request.form["filename"]}

    # Get the "img" parameter from the request and decode it with base64
    img_data = request.files["img"]
    img_base64 = img_data.read().decode("utf-8")

    # Save the image to a file in the assets folder
    path = "../assets/img/" + data["filename"]
    with open(path, "wb") as f:
        f.write(base64.decodebytes(img_base64))

    # Return a 200 status code to indicate successful upload
    return Response("Image uploaded successfully", mimetype="text/plain", status=200)
