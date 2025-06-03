import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    # Get the path from request data
    try:
        path = request.json["path"]
        if "deleted" not in request.json and "status" not in request.json:
            return "Invalid request, status or deleted field missing."
    except:  # Handle if no JSON is sent
        return "Invalid request. No path provided."

    # Delete the file if it exists
    try:
        os.remove(path)
        if "deleted" in request.json and request.json["deleted"] == "true":
            return "The file has been deleted."
        else:
            return "The file does not exist."
    except FileNotFoundError:
        return "The file does not exist."
