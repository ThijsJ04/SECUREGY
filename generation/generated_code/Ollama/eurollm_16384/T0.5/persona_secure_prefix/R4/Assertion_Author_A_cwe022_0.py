import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form.get("path")  # get the path from the form data
    if os.path.exists(path):  # check if the file exists
        os.remove(path)  # remove the file
        return "The file has been deleted"
    else:
        return "The file does not exist"
