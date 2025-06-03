from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    file_path = request.args.get(
        "file_path"
    )  # Get file path from query string or form data
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file has been deleted")
        return "Success"
    else:
        print("The file does not exist")
        return "Failure"
