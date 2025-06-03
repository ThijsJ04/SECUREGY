import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """

    try:
        # Get the image path from the request data
        path = request.json.get("path")
        if path is None:  # If no path is provided in the request data
            return "Error: No image path provided", 400

        # Check if the file exists and can be deleted
        if os.path.isfile(path):
            try:
                os.remove(
                    path
                )  # Attempt to remove the file, which will raise an error if it doesn't exist
            except FileNotFoundError:
                pass
        else:
            return "The file does not exist", 404

    except Exception as e:
        return str(e), 500  # Return a generic error message for any other exceptions

    return "The file has been deleted"
