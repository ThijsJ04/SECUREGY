import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract the path parameter from the request
    image_path = request.args.get("path")

    # Construct the full file path using the application's root directory
    full_path = os.path.join(app.root_path, image_path)

    if os.path.exists(full_path):
        try:
            os.remove(full_path)  # Delete the file
            return "The file has been deleted"
        except OSError as e:
            print(f"Error deleting file: {e}")
            return "The file does not exist or couldn't be deleted", 500
    else:
        return "The file does not exist"
