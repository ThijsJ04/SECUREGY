from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def delete_image():
    try:
        path = request.args.get("path")
        if os.path.exists(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return str(e)
