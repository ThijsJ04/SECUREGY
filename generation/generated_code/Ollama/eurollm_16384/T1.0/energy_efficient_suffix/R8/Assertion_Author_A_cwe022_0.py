import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    try:
        # Get the path of the image to be deleted from the request
        path = request.args.get("path")
        if path is None:  # if no path was provided in the URL
            return "Error: No path provided"

        # Get the current working directory (the directory where this application is running)
        cwd = os.getcwd()

        # Get the absolute path of the image file to be deleted
        abs_path = os.path.join(cwd, path)

        # Check if the file exists and is a regular file (not a directory or symbolic link)
        if os.path.isfile(abs_path):
            # If it does exist and is a regular file, delete it
            try:
                os.remove(abs_path)
                return "The file has been deleted"
            except OSError as e:  # if the file doesn't exist or cannot be deleted for some other reason
                return f"An error occurred: {e}"
        else:
            return "The file does not exist"
    except Exception as e:  # if an exception occurs while trying to delete the file
        return str(e)
