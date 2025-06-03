import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    if __name__ == "__main__":
        path = request.args.get("path")
        if os.path.exists(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
