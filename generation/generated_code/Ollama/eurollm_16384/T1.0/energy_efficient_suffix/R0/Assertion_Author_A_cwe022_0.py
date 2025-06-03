import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if request.method == "POST":
        path = request.form[
            "path"
        ]  # Get the path of the image to be deleted from the request using 'path'
        if os.path.exists(path):  # Check if the file exists
            os.remove(path)  # Delete it from the current directory
            success_message = "The file has been deleted"
        else:
            success_message = "The file does not exist"
    return success_message
