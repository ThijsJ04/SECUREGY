import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    image_path = request.args.get("path", "")
    file_to_delete = os.path.join("static/uploads", image_path)

    if os.path.exists(file_to_delete):
        try:
            os.remove(file_to_delete)
            return "The file has been deleted"
        except OSError as e:
            print(e)  # Or handle the error as needed
    return "The file does not exist"


# The rest of your code continues here...
