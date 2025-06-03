import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path or not os.path.exists(os.path.join(os.getcwd(), path)):
        return "The file does not exist"
    if not os.remove(os.path.join(os.getcwd(), path)):
        return "Failed to delete the file"
    return "The file has been deleted"
