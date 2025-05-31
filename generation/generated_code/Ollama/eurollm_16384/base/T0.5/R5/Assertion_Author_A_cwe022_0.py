import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    try:
        # Get the image path from the request
        path = request.args.get('path')
        if path is None or len(path) == 0:
            return 'The file does not exist'

        # Check if the file exists and delete it
        if os.path.exists(path):
            os.remove(path)
            return 'The file has been deleted'
        else:
            return 'The file does not exist'
    except Exception as e:
        return f'An error occurred: {str(e)}'