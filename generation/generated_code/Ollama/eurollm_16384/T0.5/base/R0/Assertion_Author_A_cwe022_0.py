import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    path = data.get("path")
    if not path:
        return "The file does not exist"

    # Check if the file exists and is a valid image file
    if os.path.isfile(path) and os.path.splitext(path)[1] in [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
    ]:
        os.remove(path)
        return "The file has been deleted"
    else:
        return "Invalid image file or file does not exist"
