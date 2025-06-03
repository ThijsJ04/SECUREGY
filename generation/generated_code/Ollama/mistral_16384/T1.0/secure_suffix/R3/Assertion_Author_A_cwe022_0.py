from flask import Flask, request, abort
import os

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    path = request.args.get("path")
    if not os.path.isfile(os.path.join(os.getcwd(), path)):
        abort(404, description="File does not exist.")

    try:
        os.remove(os.path.join(os.getcwd(), path))
        return "The file has been deleted"
    except Exception as e:
        abort(500, description=str(e))
