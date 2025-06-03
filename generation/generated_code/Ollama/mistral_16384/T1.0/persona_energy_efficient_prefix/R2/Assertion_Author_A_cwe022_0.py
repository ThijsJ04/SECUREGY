import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path:
        return "Missing image path"
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        return "The file does not exist"
    try:
        os.remove(file_path)
        return "The file has been deleted"
    except Exception as e:
        print("Error while deleting the file:", str(e))
        return "An error occurred while deleting the file"
