import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path_to_delete = request.args.get("path", "")

    # Normalize and check the file path to prevent directory traversal
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, path_to_delete)

    if not os.path.exists(file_path):
        return jsonify("The file does not exist"), 404

    try:
        os.remove(file_path)  # Delete the file if it exists
        return jsonify("The file has been deleted"), 200
    except Exception as e:
        return jsonify(f"Error deleting file: {str(e)}"), 500
