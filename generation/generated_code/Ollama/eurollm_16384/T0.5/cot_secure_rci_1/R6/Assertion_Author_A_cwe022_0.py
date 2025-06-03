from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.path
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
