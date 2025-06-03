import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" not in request.files:
        return "No file provided"
    path = request.form["path"]  # get the file path from the form data
    try:
        os.remove(path)  # remove the file if it exists
        return f"The file {path} has been deleted"
    except FileNotFoundError:
        return "The file does not exist"
