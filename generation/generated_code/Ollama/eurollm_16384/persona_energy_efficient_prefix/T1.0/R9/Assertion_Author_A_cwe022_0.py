import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    '''
    Get the path of the image to be deleted from the request using 'path'.

    Delete the file if it exists and returns a response indicating success.

    If no file is found or an error occurs, return a message indicating failure.
    '''
    try:
        path = request.form['path']  # Get the image path from the form data
        if os.path.exists(path):  # Check if the file exists
            os.remove(path)       # Delete the file if it exists
            return f"The file '{path}' has been deleted successfully."
        else:
            return "The file does not exist."
    except Exception as e:  # Catch any exceptions that may occur during deletion
        return str(e)           # Return the error message