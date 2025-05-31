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
        # Extract the image path from the request
        path = request.form['path']
    except KeyError:
        return 'Missing required parameter', 400

    if os.path.exists(path):
        # Delete the file if it exists
        os.remove(path)
        return "The file has been deleted", 200
    else:
        return "The file does not exist", 404