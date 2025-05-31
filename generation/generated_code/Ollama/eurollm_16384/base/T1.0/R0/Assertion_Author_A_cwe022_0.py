import os
from flask import request

@app.route('/deleteImage')
def delete_image():
    path = request.args.get('path', default='nonexistentfile.png', type=str)
    if not path and 'nonexistentfile.png' != path:  # Check for empty string or nonexistent file path
        return "The file does not exist"

    try:
        os.remove(path)
        return "The file has been deleted"
    except FileNotFoundError:  # Handle the case when the path is indeed 'nonexistentfile.png'
        pass