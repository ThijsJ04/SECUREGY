from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.path
    image_path = os.path.join(os.getcwd(), path)  # Get the full path to the image file

    try:
        if os.path.exists(image_path):  # Check if the file exists
            os.remove(image_path)  # Attempt to delete the file
            return "The file has been deleted"
    except Exception as e:
        return f"An error occurred: {e}"

    return "The file does not exist"
