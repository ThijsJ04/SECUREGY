import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")  # Get the file path from the request
    if not path:
        return "The file does not exist"

    file_path = os.path.join(
        os.getcwd(), path
    )  # Parse the relative path into a full absolute path
    try:
        os.remove(file_path)  # Attempt to remove the file
        return "The file has been deleted"
    except Exception as e:
        print(f"Error occurred while trying to delete {path}: {e}")
        return f"An error occurred while trying to delete {path}"  # Return an error message if the deletion fails
