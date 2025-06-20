import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the path parameter from the request
    image_path = request.args.get("path")

    # Construct the full file path using the static folder
    file_path = os.path.join(app.static_folder, "images", image_path)

    # Check if the file exists and delete it
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return "The file has been deleted"
        except OSError as e:
            print(e)  # Log any error that occurs during deletion
            return "The file could not be deleted"
    else:
        return "The file does not exist"
