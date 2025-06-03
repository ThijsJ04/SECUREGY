import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def delete_image():
    path = request.args.get(
        "path", default="nonexistentfile.jpg"
    )  # Get the path from the query string or use a default if not provided

    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Remove the file
        return f"The file '{path}' has been deleted."
    else:
        return "The file does not exist."
