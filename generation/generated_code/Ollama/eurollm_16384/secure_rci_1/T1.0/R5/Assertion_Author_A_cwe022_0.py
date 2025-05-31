import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    """
    Deletes the image from its current location.
    If an error occurs, it will return 404 Not Found status code.
    """
    try:
        # get the path of the image to be deleted from the request using 'path'
        path = request.form['path']

        if os.path.exists(path):
            # delete it from the given path in the current directory if it exists
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"An error occurred: {str(e)}", 404