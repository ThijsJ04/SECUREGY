import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' in request.form:  # Assuming the path is sent as a form parameter
        path = request.form['path']  # Get the path from the request
        if os.path.exists(path):  # Check if the file exists
            os.remove(path)  # Delete the file
            return "The file has been deleted"
        else:
            return "The file does not exist"
    else:
        return "Please provide the path of the image to be deleted"