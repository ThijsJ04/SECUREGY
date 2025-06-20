import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    image_path = request.args.get("path")  # Get the path from query parameters
    full_path = os.path.join(os.getcwd(), image_path)  # Construct full path

    if os.path.exists(full_path):
        try:
            os.unlink(full_path)  # Delete the file
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"


if __name__ == "__main__":
    app.run(debug=True)
