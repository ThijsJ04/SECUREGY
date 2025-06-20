import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path:
        return "No image path provided"

    image_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(image_path):
        return "The file does not exist"

    os.remove(image_path)
    return "The file has been deleted"
