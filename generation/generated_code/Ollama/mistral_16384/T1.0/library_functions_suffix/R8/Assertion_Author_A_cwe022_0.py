import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if not path or not os.path.isfile(os.path.join(os.getcwd(), path)):
        return "The file does not exist"
    os.remove(os.path.join(os.getcwd(), path))
    return "The file has been deleted"
