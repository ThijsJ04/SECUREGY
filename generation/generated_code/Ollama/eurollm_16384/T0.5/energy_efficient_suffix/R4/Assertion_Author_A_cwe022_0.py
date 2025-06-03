import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    if "path" in data:
        path = os.path.join(os.getcwd(), data["path"])
        if os.path.exists(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    else:
        return "Missing required parameter 'path'"
