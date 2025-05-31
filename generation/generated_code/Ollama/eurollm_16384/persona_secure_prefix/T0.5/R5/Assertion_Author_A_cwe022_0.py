import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    """Delete an image from the current directory."""
    path = request.form['path']  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):  # Check if the file exists in the current directory
        os.remove(path)  # Delete it from the given path in the current directory
        return "The file has been deleted"
    else:
        return "The file does not exist"