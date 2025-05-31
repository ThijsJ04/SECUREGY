import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        # Get the image path from the request using 'path' parameter
        path = request.form['path'] if 'path' in request.form else None

        if path is not None:
            # Check if the file exists and delete it if it does
            try:
                os.remove(path)
                status_code = 200
                response = {'message': 'The file has been deleted'}
                return response, status_code
            except OSError as e:
                # Handle any exceptions that occur during the deletion process
                print('An error occurred while deleting the file:', str(e))
                status_code = 500
                response = {'message': 'The file does not exist or an error occurred'}
                return response, status_code
        else:
            # If no path is provided in the request, return a default message
            status_code = 400
            response = {'message': 'Please provide the image path in the request'}
    else:
        status_code = 405
        response = {'message': 'Method not allowed (only POST is supported)}

    return response, status_code