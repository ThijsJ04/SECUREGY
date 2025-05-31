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
    full_path = os.path.join('.', path)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return "The file has been deleted"
        except Exception as e:
            return "The file does not exist"
    else:
        return "The file does not exist"