import os
from flask import request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    if "path" not in request.args:
        return "The file does not exist"
    path = request.args.get("path")
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred while deleting the file: {str(e)}"
    else:
        return "The file does not exist"
