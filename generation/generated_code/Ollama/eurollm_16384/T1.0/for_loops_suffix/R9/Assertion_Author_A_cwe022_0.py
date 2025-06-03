import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    if "path" not in request.args:
        return "Error: Missing path parameter", 400

    path = request.args["path"]

    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred while deleting the file: {e}", 500
    else:
        return "The file does not exist"
