import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    # Get the path parameter from the request
    path = request.args.get('path', '')

    # Construct full file path using current directory
    full_path = os.path.join('./', path)

    try:
        if os.path.exists(full_path):
            os.remove(full_path)  # or os.unlink(full_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"Error deleting file: {str(e)}"