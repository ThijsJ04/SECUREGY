from flask import request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    if "path" not in request.args or "filename" not in request.args:
        return "Missing required parameters"
    path = request.args["path"]
    filename = request.args["filename"]

    if os.path.exists(os.path.join(path, filename)):
        try:
            os.remove(os.path.join(path, filename))
        except Exception as e:
            print("Error deleting file:", str(e))
            return "The file could not be deleted"
        else:
            return "The file has been deleted"
    else:
        return "The file does not exist"
