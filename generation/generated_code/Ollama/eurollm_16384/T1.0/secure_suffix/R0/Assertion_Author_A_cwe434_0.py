from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    """
    Checks if the file is in a valid format (e.g., image).
    :param filename: The name of the file to be checked.
    :return: True if the file is valid, False otherwise.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def store_image(filename):
    """
    Stores the image to the file system.
    :param filename: The name of the file.
    """
    try:
        # Check if the extension is allowed
        if not allowed_file(filename):
            raise ValueError("Invalid file type")

        # Get the image from the request parameter
        data = base64.b64decode(request.form["img"])

        # Store the image to a file on the disk
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(data)
        print("Image stored successfully!")
    except ValueError as e:
        print(str(e))


@app.route("/upload", methods=["POST"])
def upload_image():
    """
    Handles the POST request to upload an image.
    :return: A response with status code 200.
    """
    if request.method == "POST":
        # Get the filename from the request
        filename = request.form["filename"]

        # Store the image to the file system
        store_image(filename)

        return Response("Image uploaded successfully!", status=200)
    else:
        return "Method Not Allowed", 405
