import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form.get(
        "path"
    )  # Assuming 'path' is the key for the image path in the form data
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
