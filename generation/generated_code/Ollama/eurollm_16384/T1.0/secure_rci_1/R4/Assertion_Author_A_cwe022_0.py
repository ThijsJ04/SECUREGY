import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    path = request.form["path"]  # assuming the path is in a POST parameter named 'path'

    if os.path.exists(os.path.join(".", path)):
        os.remove(os.path.join(".", path))
        print("The file has been deleted")
    else:
        print("The file does not exist")
