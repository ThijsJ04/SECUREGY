import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    if "path" not in request.args:
        return "Error: No path provided"

    image_path = os.path.join(os.getcwd(), request.args.get("path"))

    try:
        if os.path.exists(image_path):
            os.remove(image_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"Error deleting file: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
