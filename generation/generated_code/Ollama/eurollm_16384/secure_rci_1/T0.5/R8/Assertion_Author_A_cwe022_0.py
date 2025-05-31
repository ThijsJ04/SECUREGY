import os
from flask import request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    """Delete the image at the given path if it exists."""
    path = request.form.get('path')  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):
        os.remove(path)  # Delete the file at the given path if it exists
        return "The file has been deleted"
    else:
        return "The file does not exist"