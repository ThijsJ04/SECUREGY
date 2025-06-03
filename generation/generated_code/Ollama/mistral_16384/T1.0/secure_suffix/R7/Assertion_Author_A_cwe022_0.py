import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)

    if path is not None and os.path.exists(os.path.abspath(path)):
        if os.remove(path):
            return "The file has been deleted"
        else:
            return "An error occurred while deleting the file."
    else:
        return "The file does not exist"
