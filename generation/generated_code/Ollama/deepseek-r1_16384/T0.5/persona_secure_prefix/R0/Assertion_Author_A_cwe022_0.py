import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path")
    full_path = os.path.join(os.getcwd(), image_path)

    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return jsonify({"message": "The file has been deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"message": "The file does not exist"}), 404
