import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    """
    Get the path of the image to be deleted from the POST request and delete it from the given path in the current directory if it exists.
    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    try:
        # Get the image path from the POST request
        path = request.form["path"]

        # Check if the path is valid (should be a string)
        if not isinstance(path, str):
            return "Invalid path format."

        # Convert the path to lowercase for case-insensitive comparison
        path = path.lower()

        # Get the current directory path
        current_dir = os.getcwd()

        # Check if the image exists in the current directory
        if os.path.exists(os.path.join(current_dir, path)):
            # Delete the file
            os.remove(os.path.join(current_dir, path))

            return "The file has been deleted."
        else:
            return f"The file '{path}' does not exist."
    except Exception as e:
        return str(e)
