import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)

    if not path:
        return "Missing 'path' parameter in the request"

    file_path = os.path.join(os.getcwd(), path)

    if os.path.exists(file_path):
        os.remove(file_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
