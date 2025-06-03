import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.args.get(
        "path"
    )  # Assuming 'path' parameter is in GET request URL with key 'path'
    file_to_delete = os.path.join(os.getcwd(), path)

    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        return "The file has been deleted"
    else:
        return "The file does not exist"
