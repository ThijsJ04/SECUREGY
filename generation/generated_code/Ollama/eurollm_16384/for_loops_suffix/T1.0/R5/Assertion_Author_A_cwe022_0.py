import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    # Get the file path from the POST request data
    try:
        path = request.form.get('path')  # Assuming the 'path' parameter is sent in the form data
        # Check if the path exists and delete the file
        if os.path.exists(path):
            os.remove(path)
            status_message = "The file has been deleted"
        else:
            status_message = "The file does not exist"
    except Exception as e:
        status_message = str(e)  # Catch any other exceptions that might occur

    return status_message