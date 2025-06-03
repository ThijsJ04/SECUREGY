import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    path = request.form[
        "path"
    ]  # Get the path of the image to be deleted from the request using 'path'
    file_path = os.path.join(
        os.getcwd(), path
    )  # Join the current directory with the file path and get the full path

    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)  # Delete the file if it exists and is a regular file
            return "The file has been deleted"
        else:
            print("This is not a file.")
    else:
        print("The file does not exist.")
        return "The file does not exist"
