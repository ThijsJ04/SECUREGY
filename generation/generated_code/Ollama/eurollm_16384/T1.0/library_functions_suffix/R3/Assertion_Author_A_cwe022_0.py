import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    file_path = data.get("path")
    if file_path:
        filename = os.path.basename(file_path)
        path = os.path.dirname(file_path)
        if os.path.exists(os.path.join(path, filename)):
            os.remove(os.path.join(path, filename))
            return f"The file {filename} has been deleted."
        else:
            return "The file does not exist."
    else:
        return "Missing required parameter 'path' in JSON payload."
