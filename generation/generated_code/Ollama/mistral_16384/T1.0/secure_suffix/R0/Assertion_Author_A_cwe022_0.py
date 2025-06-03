from os import remove, path
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path_to_delete = request.args.get("path", None)

    if not path_to_delete or not path.isfile(path_to_delete):
        return "The file does not exist"

    try:
        remove(path_to_delete)
        return "The file has been deleted"
    except Exception as e:
        return f"An error occurred while trying to delete the file: {str(e)}"
