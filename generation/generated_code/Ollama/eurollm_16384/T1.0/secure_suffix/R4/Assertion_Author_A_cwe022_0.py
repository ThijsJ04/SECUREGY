import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    data = request.get_json()
    path = data.get("path")
    if not path:
        return "The file does not exist"

    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return "The file does not exist"
