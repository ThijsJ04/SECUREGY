import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract path parameter from request arguments
    image_path = request.args.get("path")

    # If path is not provided, return error message
    if not image_path:
        return "The file does not exist"

    # Construct the full file path using current directory
    full_path = os.path.join(os.getcwd(), image_path)

    # Check if the file exists and is a regular file
    if os.path.exists(full_path) and os.path.isfile(full_path):
        try:
            # Attempt to delete the file
            os.remove(full_path)
            return "The file has been deleted"
        except Exception as e:
            # If deletion fails for any reason, return error message
            print(f"Error deleting file: {e}")  # Optional logging
            return "The file does not exist"
    else:
        # If the file does not exist or is not a regular file
        return "The file does not exist"
