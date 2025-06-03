import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" in request.form:  # Assuming the path is sent as a form parameter
        path = request.form["path"]
        if os.path.exists(path):
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
        else:
            print("The file does not exist")
            return "The file does not exist"
    else:
        print("No path provided in the request")
        return "No path provided in the request"
