from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    data = request.get_json()
    if "path" not in data:
        return "Missing path parameter"

    file_path = os.path.join(os.getcwd(), data["path"])

    # Check if the file exists before deletion
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred while deleting the file: {e}"
    else:
        return "The file does not exist"
