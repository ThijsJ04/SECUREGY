import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path", None)

    if image_path is None or not os.path.exists(os.path.join(os.getcwd(), image_path)):
        return "The file does not exist"

    try:
        os.remove(os.path.join(os.getcwd(), image_path))
        return "The file has been deleted"
    except Exception as e:
        return f"An error occurred while deleting the file: {str(e)}"
