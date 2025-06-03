import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract path parameter from request
    path = request.args.get("path")

    # Check if file exists
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted", 200
        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    else:
        return "The file does not exist", 404


if __name__ == "__main__":
    app.run(debug=True)
