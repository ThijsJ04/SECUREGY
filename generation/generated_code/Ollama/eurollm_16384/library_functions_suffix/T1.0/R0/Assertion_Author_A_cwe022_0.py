import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    try:
        # Get the path of the image to be deleted from the request using 'path' parameter
        path = request.args.get('path')
        if not path or len(path) == 0:
            return "The file does not exist"

        # Delete the image if it exists in the current directory
        os.remove(path)
        return "The file has been deleted"
    except Exception as e:
        # Handle any exceptions that may occur during file deletion
        print("An error occurred while trying to delete the file", str(e))
        return "An error occurred"