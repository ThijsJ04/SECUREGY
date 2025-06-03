import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", "")
    if not path:
        return "The file does not exist"

    images_dir = "images"
    abs_images_dir = os.path.abspath(images_dir)
    full_path = os.path.join(abs_images_dir, path)
    real_path = os.path.realpath(full_path)

    if not real_path.startswith(abs_images_dir):
        return "The file does not exist"

    if os.path.exists(real_path):
        os.remove(real_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
