import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if not os.path.exists(path):
        return "The file does not exist"
    else:
        os.remove(path)
        return "The file has been deleted"
