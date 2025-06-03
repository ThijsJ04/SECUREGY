from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.form.get("path")  # Get the path of the image from the request
    if not path:
        return "No file path provided"

    file_to_delete = os.path.join(os.getcwd(), path)

    if os.path.exists(file_to_delete):  # Check if the file exists at that path
        try:
            os.remove(
                file_to_delete
            )  # Delete the file from the given path in the current directory
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
            return f"An error occurred while deleting the file: {e}", 500
        else:
            return "The file has been deleted"
    else:
        return "The file does not exist"
