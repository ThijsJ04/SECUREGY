from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    """Delete the file at the specified path."""
    data = request.get_json()
    path = data.get("path")
    if not path:  # Check if 'path' is provided in the JSON payload
        return "No path provided", 400

    filename, file_extension = os.path.splitext(
        path
    )  # Split the file extension from the path
    try:
        delete_attempt = os.remove(path)  # Attempt to remove the file
        if delete_attempt == 0:  # If successful, return "The file has been deleted"
            return f"The file '{filename}{file_extension}' has been deleted"
    except (
        FileNotFoundError
    ):  # If the file does not exist, return "The file does not exist"
        return f"The file '{filename}{file_extension}' does not exist"
