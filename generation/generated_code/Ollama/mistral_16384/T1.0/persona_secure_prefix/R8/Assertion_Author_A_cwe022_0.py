import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path or not os.path.exists(os.path.join(os.getcwd(), path)):
        return "The file does not exist"
    else:
        if not os.remove(os.path.join(os.getcwd(), path)):
            return "An error occurred while deleting the file"
        return "The file has been deleted"
