import os

from flask import Flask, request

app = Flask(__name__)


def deleteImage(path):
    try:
        os.remove(path)
        return f"The file {path} has been deleted"
    except FileNotFoundError:
        return "The file does not exist"


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path'.
    Delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
