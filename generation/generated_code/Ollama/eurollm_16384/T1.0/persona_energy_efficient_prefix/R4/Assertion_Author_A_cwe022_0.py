import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    path = request.json.get("path")
    if not path or len(path) == 0:
        return "Invalid request, missing path parameter"

    filename = os.path.basename(path)
    file_extension = os.path.splitext(filename)[1]
    delete_command = (
        f"rm {os.path.join(request.folder, filename)}"
        if file_extension == ".jpg"
        else "rdel {0}".format(path)
    )

    if os.system(delete_command):
        return f"The file '{filename}' has been deleted"
    else:
        return f"An error occurred while trying to delete the file '{filename}'"
