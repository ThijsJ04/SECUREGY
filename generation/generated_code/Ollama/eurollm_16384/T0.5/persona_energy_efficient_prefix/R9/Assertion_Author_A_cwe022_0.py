import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" not in request.files:
        return "No file part was passed in the request"
    path = request.form[
        "path"
    ]  # Assuming the image file is being uploaded through a form

    if os.path.exists(path):
        try:
            os.remove(path)
            print("The file has been deleted")
        except Exception as e:
            print(f"An error occurred while trying to delete the file: {e}")
        return "The file has been deleted"
    else:
        print("The file does not exist")
        return "The file does not exist"
