import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    if "path" not in request.files:
        return "No file part"
    path = request.form["path"]  # Assuming the image path is sent as a form parameter

    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file '{path}' has been deleted"
        except Exception as e:
            print("An error occurred while deleting the file:", str(e))
            return "Failed to delete the file"
    else:
        return "The file does not exist"
