import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path")
    if os.path.exists(image_path):
        os.remove(image_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"


if __name__ == "__main__":
    app.run(debug=True)
