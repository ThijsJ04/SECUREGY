import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the path parameter from the request arguments
    image_path = request.args.get("path")

    # Check if the file exists
    if os.path.exists(image_path):
        try:
            os.remove(image_path)  # Delete the file
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"
