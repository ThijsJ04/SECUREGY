import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' not in request.files:
        return "No file uploaded"
    path = request.form["path"]
    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file {path} has been deleted"
        except Exception as e:
            return str(e)
    else:
        return "The file does not exist"