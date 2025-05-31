from flask import request
import os

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path of the image from the request using 'path'
    if not os.path.exists(path):  # Check if the file exists at that path
        return "The file does not exist"
    os.remove(path)  # Delete the file if it exists
    return "The file has been deleted"