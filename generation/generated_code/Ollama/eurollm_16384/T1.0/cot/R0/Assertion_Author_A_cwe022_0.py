from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.args.get("path")  # Get the path from the query parameter
    if os.path.exists(path):  # Check if the file exists in the current directory
        os.remove(path)  # Delete the file if it exists
        return f"The file has been deleted: {path}"
    else:
        return "The file does not exist"
