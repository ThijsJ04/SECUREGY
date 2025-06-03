from flask import jsonify
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    # Get path of image to be deleted from the request using 'path' parameter
    try:
        path = request.args.get("path")
        if not path:
            return jsonify({"error": "Missing 'path' parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Check if the given path is a directory and the file exists at that path
    current_dir = os.getcwd()
    if not os.path.isdir(current_dir):
        return jsonify({"error": "Invalid directory"}), 400
    file_path = os.path.join(current_dir, path)
    try:
        os.remove(file_path)
        status = "The file has been deleted"
    except Exception as e:
        status = "An error occurred while deleting the file"
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": status}), 200
