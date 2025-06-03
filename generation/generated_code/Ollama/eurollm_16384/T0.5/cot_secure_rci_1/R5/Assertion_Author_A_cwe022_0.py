from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    path = request.args.get("path")
    if path:  # Make sure 'path' is not empty
        file_path = os.path.join(
            os.getcwd(), path
        )  # Join the current directory with the file path
        if os.path.exists(file_path):  # Check if the file exists
            try:
                os.remove(file_path)  # Delete the file
                return "The file has been deleted"
            except Exception as e:
                print("Error deleting file:", str(e))
                return "An error occurred while deleting the file."
        else:
            return "The file does not exist"
    else:
        return "No path provided"
