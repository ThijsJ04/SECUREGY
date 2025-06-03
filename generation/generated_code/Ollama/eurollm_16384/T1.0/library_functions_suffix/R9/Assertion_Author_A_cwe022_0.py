import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    """
    Deletes the image with the specified path from the current directory if it exists.

    Args:
        None
    Returns:
        str: The message "The file has been deleted" or "The file does not exist".
    """
    path = request.args.get("path")  # get image path from query string

    if os.path.exists(path):  # if the file exists
        os.remove(path)
        return f"The file has been deleted"
    else:
        return "The file does not exist"
