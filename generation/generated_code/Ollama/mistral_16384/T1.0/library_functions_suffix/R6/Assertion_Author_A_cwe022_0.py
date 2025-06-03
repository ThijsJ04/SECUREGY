import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if path is None:
        return "Please provide a valid image path.", 400

    image_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(image_path):
        return "The file does not exist", 404

    try:
        os.remove(image_path)
        return "The file has been deleted"
    except Exception as e:
        return str(e), 500
