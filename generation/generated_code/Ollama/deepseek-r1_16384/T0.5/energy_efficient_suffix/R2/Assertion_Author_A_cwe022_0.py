import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    path = request.args.get("path")  # Get path parameter from query string
    full_path = os.path.join(os.getcwd(), path)  # Construct full file path

    try:
        if os.path.exists(full_path):
            os.unlink(full_path)  # Delete the file
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"The file could not be deleted: {str(e)}"
