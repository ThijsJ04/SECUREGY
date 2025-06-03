import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get(
        "path", default="None"
    )  # Get the path from the URL query string or use a default value if not provided
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Remove the file
        return "The file has been deleted"
    else:
        return "The file does not exist"
