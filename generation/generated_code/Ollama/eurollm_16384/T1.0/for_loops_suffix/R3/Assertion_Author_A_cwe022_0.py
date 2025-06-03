import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", default=None, type=str)
    if path and os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
