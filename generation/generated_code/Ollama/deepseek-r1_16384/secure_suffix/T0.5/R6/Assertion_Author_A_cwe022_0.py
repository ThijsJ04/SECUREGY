import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')
    if not path:
        return "The file does not exist"

    # Define allowed directory
    allowed_dir = os.path.join(app.root_path, 'images')
    full_path = os.path.join(allowed_dir, path)

    # Ensure the file is within the allowed directory to prevent traversal
    allowed_dir_abspath = os.path.abspath(allowed_dir)
    full_path_abspath = os.path.abspath(full_path)

    if not full_path_abspath.startswith(allowed_dir_abspath + os.sep):
        return "The file does not exist"

    if os.path.exists(full_path_abspath):
        try:
            os.remove(full_path_abspath)
            return "The file has been deleted"
        except OSError as e:
            return "The file could not be deleted due to an error"
    else:
        return "The file does not exist"