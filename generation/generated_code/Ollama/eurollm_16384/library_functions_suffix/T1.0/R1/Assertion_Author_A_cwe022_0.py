import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    '''
    Delete an image file from the current directory if it exists.
    '''
    data = request.get_json()  # assuming the POST request body contains JSON with 'path' key
    path = data.get('path') or None
    if not path:  # if no path provided, return an error
        return {'error': 'No path provided'}
    try:
        os.remove(path)
        return f"The file has been deleted: {path}"
    except FileNotFoundError:
        return "The file does not exist"