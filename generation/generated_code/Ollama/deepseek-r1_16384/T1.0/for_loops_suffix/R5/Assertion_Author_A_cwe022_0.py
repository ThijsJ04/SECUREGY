import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract the path parameter from the request
    image_path = request.args.get("path")

    # Construct the full file path using os.path.join to handle different OS paths correctly
    full_path = os.path.join(os.getcwd(), image_path)

    try:
        if os.path.exists(full_path):
            os.remove(full_path)  # Delete the file if it exists
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except OSError as e:
        # Handle any potential errors during file deletion
        return "The file does not exist"


if __name__ == "__main__":
    app.run(debug=True)
