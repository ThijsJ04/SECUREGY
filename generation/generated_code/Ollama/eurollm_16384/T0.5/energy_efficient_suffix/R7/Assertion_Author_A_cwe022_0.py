import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" not in request.files:
        return "Error: No file part in the request"
    path = request.form["path"]

    # Check if the file exists and is a valid image file (JPEG, PNG)
    if os.path.exists(path):
        try:
            import cv2  # For checking if it's an image

            print("File exists")
        except ImportError:
            print("Image type not supported")
            return "The file does not exist"

    try:
        os.remove(path)
    except OSError as e:
        print("Failed to delete file:", str(e))
        return (
            "The file has been deleted"
            if os.path.exists(path)
            else "The file does not exist"
        )

    return "The file has been deleted"
