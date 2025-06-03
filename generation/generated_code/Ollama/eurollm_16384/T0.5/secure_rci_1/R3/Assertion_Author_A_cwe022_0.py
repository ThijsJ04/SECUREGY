import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    if "path" in request.args:
        path = request.args["path"]
        if os.path.exists(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    else:
        return "You must provide the 'path' parameter in your request."
