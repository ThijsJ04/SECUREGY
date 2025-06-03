import os
from flask import request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if "path" not in request.form:
        return "Error: Missing path parameter"
    path = request.form["path"]

    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred while trying to delete the file: {str(e)}"
    else:
        return "The file does not exist"
