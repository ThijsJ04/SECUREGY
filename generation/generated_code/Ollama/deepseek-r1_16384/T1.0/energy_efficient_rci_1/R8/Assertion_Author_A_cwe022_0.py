import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path", "")
    full_path = os.path.join(os.getcwd(), image_path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return "The file has been deleted"
        except OSError as e:
            return f"The file does not exist or couldn't be deleted: {e}"
    else:
        return "The file does not exist"
