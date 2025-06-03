import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    if "path" not in request.args:
        return "Error: No path provided"
    path = request.args["path"]
    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file '{path}' has been deleted"
        except Exception as e:
            return f"An error occurred while deleting the file: {str(e)}"
    else:
        return "The file does not exist"
