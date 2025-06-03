import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" not in request.files:
        return "No file part"
    path = request.form["path"]
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            print("Error occurred while deleting the file:", str(e))
            return "An error occurred while deleting the file"
    else:
        return "The file does not exist"
