import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    image_path = data.get("path")

    if image_path and os.path.exists(image_path):
        os.remove(image_path)
        print("The file has been deleted")
        return "The file has been deleted"
    else:
        print("The file does not exist")
        return "The file does not exist"
