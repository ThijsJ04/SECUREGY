import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    data = request.get_json()
    if "path" not in data:
        return "Missing path parameter", 400
    path = data["path"]
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            print(f"Error deleting file: {e}")
            return f"An error occurred while trying to delete the file: {str(e)}", 500
    else:
        return "The file does not exist"
