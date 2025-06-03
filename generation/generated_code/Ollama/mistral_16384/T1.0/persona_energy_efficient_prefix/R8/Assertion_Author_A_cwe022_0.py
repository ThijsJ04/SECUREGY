import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path:
        return "No image path provided"
    image_path = os.path.join(os.getcwd(), path)
    if os.path.isfile(image_path):
        os.remove(image_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
