import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    # Get the image path from the request using 'path' parameter
    path = request.args.get("path")

    # Check if the path is valid (either a string or None)
    if not isinstance(path, str):
        return "Error: Invalid image path", 400

    # Try to delete the file using its path
    try:
        os.remove(path)
        return f"The file '{path}' has been deleted."
    except FileNotFoundError:
        return "The file does not exist."
