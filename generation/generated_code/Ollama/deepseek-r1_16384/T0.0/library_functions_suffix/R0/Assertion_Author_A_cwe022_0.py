import os

from flask import Flask, request
from flask import jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the path parameter from the request
    image_path = request.args.get("path")

    # Check if the file exists
    if os.path.exists(image_path):
        try:
            # Delete the file
            os.remove(image_path)
            message = "The file has been deleted"
            status_code = 200
        except Exception as e:
            message = f"Error deleting file: {str(e)}"
            status_code = 500
    else:
        message = "The file does not exist"
        status_code = 404

    # Return a JSON response with the message and status code
    return jsonify({"message": message}), status_code
