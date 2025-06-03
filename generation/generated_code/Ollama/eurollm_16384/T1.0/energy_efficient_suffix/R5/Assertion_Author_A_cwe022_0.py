from flask import Flask, request, abort
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    if not request.args.get("path"):
        abort(400, "Missing path parameter")
    try:
        file_path = os.path.join(os.getcwd(), request.args.get("path"))
        if os.path.exists(file_path) and os.path.isfile(file_path):
            if not confirm():
                return "The file has been deleted."
            os.remove(file_path)
            return "The file does not exist."
    except Exception as e:
        abort(500, str(e))
