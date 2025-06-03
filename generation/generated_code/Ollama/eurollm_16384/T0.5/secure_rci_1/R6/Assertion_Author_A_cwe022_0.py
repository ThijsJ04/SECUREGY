import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if request.method == "POST":
        file_path = request.form[
            "path"
        ]  # Get the path of the image to be deleted from the request using 'path'
        try:
            os.remove(file_path)  # Attempt to delete the file at the given path
            print("The file has been deleted")
        except FileNotFoundError:
            print("The file does not exist")
    return (
        "The file has been deleted"
        if os.path.exists(file_path)
        else "The file does not exist"
    )  # Return the result of the deletion operation
