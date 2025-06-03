import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    path = request.form.get("path")  # Get the image path from the form data
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete the file
        return "The file has been deleted"
    else:
        return "The file does not exist"
