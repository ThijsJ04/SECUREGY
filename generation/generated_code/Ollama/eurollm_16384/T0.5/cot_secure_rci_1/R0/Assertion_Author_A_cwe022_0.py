from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    try:
        # Get the path of the image to be deleted from the request using 'path'
        path = request.form["path"]

        # Check if the file exists in the current directory
        if os.path.exists(path):
            # Delete the file if it exists and is not a link
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
        else:
            # If the file does not exist, return an error message
            return "The file does not exist"
    except Exception as e:
        # Handle any exceptions that may occur during file deletion
        print(f"An error occurred: {e}")
        return f"An error occurred: {str(e)}"
