import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    if "path" in data and os.path.exists(data["path"]):
        os.remove(data["path"])
        return "The file has been deleted"
    else:
        return "The file does not exist or is missing the required parameter"
