import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    path = request.args.get("path")
    if not path:
        return "The file does not exist"

    # Construct the full file path
    file_path = os.path.join(app.root_path, "images", path)

    if os.path.exists(file_path):
        try:
            os.unlink(file_path)  # Use unlink to delete the file
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"


if __name__ == "__main__":
    app.run(debug=True)
