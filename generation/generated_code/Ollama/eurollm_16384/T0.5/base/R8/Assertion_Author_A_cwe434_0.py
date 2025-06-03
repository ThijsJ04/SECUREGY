from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = (
    "../assets/img"  # Change this to the actual path where you want to store the images
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    """
    Check if the file is a valid image.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_img():
    if "filename" not in request.files:
        return Response("No file part")
    file = request.files["img"]
    filename = secure_filename(file.filename)
    allowed_extensions = ALLOWED_EXTENSIONS
    if file and allowed_extensions.__contains__(
        file.filename.rsplit(".", 1)[1].lower()
    ):
        if "." in filename:
            # Remove the extension from the filename if it already exists
            filename = os.path.splitext(filename)[0] + ".png"
        else:
            filename += ".png"  # Add .png extension if not present
        print("File Name:", filename)
    else:
        return Response("Invalid file type")
    print("Filename:", filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return Response("Image uploaded successfully!", status=201)


if __name__ == "__main__":
    app.run()
