from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path:  # Check if 'path' is provided in the request
        return "Error: No image path provided"

    if os.path.exists(path):  # Check if the file exists at that path
        try:
            os.remove(path)  # Attempt to delete the file
            return "The file has been deleted"
        except OSError as e:  # Handle any exceptions that may occur during deletion
            print("An error occurred while trying to delete the file:", str(e))
            return f"Failed to delete the file: {str(e)}"
    else:  # File does not exist, return a message indicating this
        return "The file does not exist"