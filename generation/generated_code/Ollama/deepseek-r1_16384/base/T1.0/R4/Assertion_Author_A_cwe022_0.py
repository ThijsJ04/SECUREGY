import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')  # Get 'path' parameter from request
    if not path:
        return "The file does not exist"  # Return error if path is missing

    full_path = os.path.join(os.getcwd(), path)  # Construct full path safely
    if not os.path.exists(full_path):
        return "The file does not exist"

    try:
        os.unlink(full_path)  # Delete the file
        return "The file has been deleted"
    except Exception as e:
        print(f"Error deleting file: {e}")  # Log any deletion errors
        return "The file does not exist"