import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path", "")
    if not image_path:
        return "The file does not exist"
    full_path = os.path.join(os.getcwd(), image_path)
    if not os.path.exists(full_path):
        return "The file does not exist"
    try:
        os.remove(full_path)
        return "The file has been deleted"
    except Exception as e:
        return "The file does not exist"
