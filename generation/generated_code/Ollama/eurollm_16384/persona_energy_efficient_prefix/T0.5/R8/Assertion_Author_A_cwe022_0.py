import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' not in request.files:
        return 'No file part in the request'
    path = str(request.form['path'])  # Assuming the file path is a form input
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except OSError as e:
            print('An error occurred:', str(e))
            return 'An error occurred while deleting the file'
    else:
        return "The file does not exist"