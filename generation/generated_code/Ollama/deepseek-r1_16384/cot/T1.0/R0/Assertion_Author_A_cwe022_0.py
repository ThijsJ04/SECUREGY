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
    image_path = request.args.get('path')

    # Construct the full file path using os.path.join for safety
    full_path = os.path.join(os.getcwd(), image_path)

    if os.path.exists(full_path):
        try:
            # Delete the file
            os.unlink(full_path)
            return "The file has been deleted"
        except Exception as e:
            return f"An error occurred while deleting the file: {str(e)}"
    else:
        return "The file does not exist"