from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.args.get(
        "path"
    )  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):  # Check if the file exists at the specified path
        os.remove(path)  # Delete the file
        return "The file has been deleted"
    else:
        return "The file does not exist"
