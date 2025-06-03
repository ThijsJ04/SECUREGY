import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    image_path = request.args.get("path")

    if not image_path:
        return "No image path provided in the request"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    full_image_path = os.path.join(current_directory, image_path)

    if os.path.exists(full_image_path) and os.path.isfile(full_image_path):
        os.unlink(full_image_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
