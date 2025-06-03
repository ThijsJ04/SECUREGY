from flask import Flask, request, Response
import base64
from io import BytesIO
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png".
    :return: a Response with status code equals to 200.
    """
    # Get the filename from the request
    filename = request.args.get("filename")

    # If no filename is provided, return an error message
    if not filename:
        return {"error": "Filename must be provided"}, 400

    # Get the image data from the request
    try:
        img_data = base64.b64decode(request.form["img"]).decode("utf-8")
    except KeyError:
        return {"error": "No image provided"}, 400

    # Create a BytesIO object to read the image data
    content = BytesIO()

    # Write the image data to the BytesIO object
    content.write(img_data)

    # Save the image to the file "../assets/img/{filename}.png"
    with open("../assets/img/" + filename + ".png", "wb") as f:
        f.write(content.getvalue())

    return {"message": "Image uploaded successfully"}, 201
