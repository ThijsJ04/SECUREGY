import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', '')
    if not path:
        return "The file does not exist"
    full_path = os.path.join(os.getcwd(), path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return "The file has been deleted"
        except PermissionError:
            return "Permission denied to delete the file"
        except IsADirectoryError:
            return "Cannot delete a directory"
    else:
        return "The file does not exist"