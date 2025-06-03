import os

from flask import Flask, request
from flask.json import jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the path parameter from the request
    image_path = request.args.get("path", "")

    # Construct the full file path
    full_path = os.path.join(os.getcwd(), image_path)

    # Check if the file exists and delete it if it does
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return jsonify("The file has been deleted")
        except Exception as e:
            return jsonify(f"Error deleting file: {str(e)}"), 500
    else:
        return jsonify("The file does not exist")
