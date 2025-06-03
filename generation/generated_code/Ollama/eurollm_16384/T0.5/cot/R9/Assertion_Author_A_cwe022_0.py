from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.args.get("path")  # Get the path of the image from the query string
    if os.path.exists(path):  # Check if the file exists at the given path
        os.remove(path)  # Delete the file
        return f"The file '{path}' has been deleted."
    else:
        return "The file does not exist."
