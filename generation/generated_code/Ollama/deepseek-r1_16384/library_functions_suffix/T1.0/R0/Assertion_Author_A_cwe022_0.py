import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['DELETE'])
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    # Extract path parameter from request
    img_path = request.args.get('path')

    # Check if path is provided
    if not img_path:
        return "Please provide the image path", 400

    # Construct full file path using current directory and given path
    full_path = os.path.join(os.getcwd(), img_path)

    try:
        # Check if file exists and delete it
        if os.path.exists(full_path):
            os.remove(full_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except OSError as e:
        return f"Error deleting file: {str(e)}", 500