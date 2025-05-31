import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    try:
        # Get the path of the image to be deleted from the request using 'path'
        path = request.form['path']

        # Check if the path is valid
        if not os.path.exists(path):
            return "The file does not exist"

        # Delete the file if it exists
        os.remove(path)

        return "The file has been deleted"
    except Exception as e:
        return str(e)