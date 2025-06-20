import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.form.get("path", "")
    full_path = os.path.join(os.getcwd(), path)
    if os.path.exists(full_path) and os.path.isfile(full_path):
        os.remove(full_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
