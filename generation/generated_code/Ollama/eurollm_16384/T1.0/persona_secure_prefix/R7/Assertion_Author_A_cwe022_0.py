import os
from flask import request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    path = request.json.get("path")
    if not path:  # Ensure 'path' is defined in the JSON payload
        return "Missing 'path' field", 400

    try:
        print(
            os.path.exists(path)
        )  # Print the existence of the file for testing purposes
        os.remove(path)
        return "The file has been deleted"
    except OSError as e:
        return f"Failed to delete file: {str(e)}", 500
