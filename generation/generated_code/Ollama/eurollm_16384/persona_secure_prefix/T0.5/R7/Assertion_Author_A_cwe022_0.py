import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' in request.form:
        path = request.form.get('path')  # Get the image path from the POST request
        filename, extension = os.path.splitext(path)
        file_to_delete = filename + extension
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)  # Delete the file if it exists
            return 'The file has been deleted'
        else:
            return 'The file does not exist'
    else:
        return 'Missing path parameter'