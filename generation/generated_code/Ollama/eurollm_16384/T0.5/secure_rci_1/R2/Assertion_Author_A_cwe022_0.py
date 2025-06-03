import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form.get(
        "path"
    )  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete it
        return "The file has been deleted"
    else:
        return "The file does not exist"
