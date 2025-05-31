import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', None)
    if not path:
        return "Missing 'path' parameter"

    file_path = os.path.join(os.getcwd(), path)
    if not os.path.exists(file_path):
        return "The file does not exist"

    if not os.remove(file_path):
        return "Failed to delete the file"

    return "The file has been deleted"