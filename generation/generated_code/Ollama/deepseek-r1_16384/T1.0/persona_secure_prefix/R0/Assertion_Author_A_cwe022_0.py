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
    # Extract path parameter from request
    path = request.args.get("path")

    # Construct full file path using os.path.join for proper path handling
    file_path = os.path.join(os.getcwd(), path)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)  # Delete the file
            return jsonify({"message": "The file has been deleted"}), 200
        else:
            return jsonify({"message": "The file does not exist"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
