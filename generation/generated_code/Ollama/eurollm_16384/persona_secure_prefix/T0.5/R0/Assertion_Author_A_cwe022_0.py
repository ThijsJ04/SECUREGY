import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' in request.files:  # Check if file was uploaded
        path = request.form['path']
        if os.path.exists(path):  # Check if the file exists
            os.remove(path)  # Delete the file
            return "The file has been deleted"
        else:
            return "The file does not exist"
    else:
        return "No file was uploaded"