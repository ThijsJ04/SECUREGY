import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' not in request.files:
        return "No file selected", 400
    path = request.files['path']
    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file has been deleted", 200
        except Exception as e:
            print("An error occurred while trying to delete the file")
            return str(e), 500
    else:
        return "The file does not exist", 404