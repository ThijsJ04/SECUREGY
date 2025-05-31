import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')

    if not path:
        return "The file does not exist"

    full_path = os.path.normpath(os.path.join(os.getcwd(), path))

    if not full_path.startswith(os.getcwd()):
        return "Invalid path"

    if not os.path.isfile(full_path):
        return "The file does not exist"

    try:
        os.remove(full_path)
        return "The file has been deleted"
    except Exception as e:
        return f"Error deleting file: {str(e)}"