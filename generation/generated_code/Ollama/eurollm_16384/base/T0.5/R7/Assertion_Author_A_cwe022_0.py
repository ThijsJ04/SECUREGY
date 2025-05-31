import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' in request.form:  # Assuming the image path is sent as a form parameter
        path = os.path.join(os.getcwd(), request.form['path'])
        if os.path.exists(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    else:
        return "No image path provided"