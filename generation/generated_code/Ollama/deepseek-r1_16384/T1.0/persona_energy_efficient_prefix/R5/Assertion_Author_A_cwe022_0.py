import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if not path:
        return "The file does not exist"

    file_path = os.path.join(os.getcwd(), path)
    if os.path.isfile(file_path):
        os.unlink(file_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
