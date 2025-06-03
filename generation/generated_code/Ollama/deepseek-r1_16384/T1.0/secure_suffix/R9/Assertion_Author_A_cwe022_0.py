import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    path = request.args.get("path", "")
    if not path:
        return "The file does not exist"

    current_dir = os.path.abspath(os.getcwd())
    full_path = os.path.join(current_dir, path)
    normalized_full_path = os.path.normpath(full_path)

    if not normalized_full_path.startswith(current_dir):
        return "The file does not exist"

    if os.path.exists(normalized_full_path) and os.path.isfile(normalized_full_path):
        try:
            os.remove(normalized_full_path)
            return "The file has been deleted"
        except OSError as e:
            if e.errno == 2:  # ENOENT, file not found
                return "The file does not exist"
            else:
                app.logger.error(f"Error deleting file {normalized_full_path}: {e}")
                return "Failed to delete the file", 500
    else:
        return "The file does not exist"
