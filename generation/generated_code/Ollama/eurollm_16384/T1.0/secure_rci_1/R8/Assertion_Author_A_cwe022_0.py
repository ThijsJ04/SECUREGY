from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form["path"]  # Get the file path from the request
    if not os.path.exists(path):
        return "The file does not exist."
    else:
        try:
            os.remove(path)
            return "The file has been deleted."
        except Exception as e:
            return f"An error occurred: {str(e)}"
