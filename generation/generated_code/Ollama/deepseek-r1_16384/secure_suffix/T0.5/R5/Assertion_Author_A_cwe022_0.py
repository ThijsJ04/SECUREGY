import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    path = request.args.get('path')
    if not path:
        return "The file does not exist"

    # Validate that the path is within the current directory to prevent directory traversal attacks
    abspath = os.path.abspath(path)
    current_dir = os.path.abspath(os.getcwd())
    if not abspath.startswith(current_dir):
        return "Invalid path"

    try:
        if os.path.exists(abspath):
            os.remove(abspath)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"Error deleting file: {str(e)}"