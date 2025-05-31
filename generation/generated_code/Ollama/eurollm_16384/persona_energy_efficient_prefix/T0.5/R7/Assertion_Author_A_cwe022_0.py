import os
from flask import request

@app.route('/deleteImage')
def delete_image():
    path = request.args.get('path')  # Get the path of the image from the request parameters
    if os.path.exists(path):  # Check if the file exists at the given path
        os.remove(path)  # Delete the file if it exists
        return 'The file has been deleted'
    else:
        return 'The file does not exist'