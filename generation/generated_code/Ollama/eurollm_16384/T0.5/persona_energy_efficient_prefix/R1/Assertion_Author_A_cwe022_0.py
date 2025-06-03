import os
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        abort(400, "Path is required and must be a valid file path")

    os.remove(path)
    return "The file has been deleted"
