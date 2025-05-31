import os
from flask import request

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete it from the given path in the current directory
        return f"The file has been deleted"
    else:
        return "The file does not exist"