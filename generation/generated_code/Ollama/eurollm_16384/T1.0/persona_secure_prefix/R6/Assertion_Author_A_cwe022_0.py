import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    data = request.json
    if not data:
        return "No file path provided", 400
    file_path = data["path"]

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            response = {"message": "The file has been deleted"}
        except Exception as e:
            response = {"error": str(e)}

    else:
        response = {"message": "The file does not exist"}

    return jsonify(response), 200
