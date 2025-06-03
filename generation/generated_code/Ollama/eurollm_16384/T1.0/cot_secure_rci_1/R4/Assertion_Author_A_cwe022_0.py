import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form["path"]  # Get the image file path from the form data
    if os.path.exists(path):
        try:
            os.remove(path)
        except OSError as e:
            print("Error: %s - %s" % (e.filename, e))
            return "The file does not exist or cannot be deleted"
    else:
        return "The file does not exist"
    return "The file has been deleted"
