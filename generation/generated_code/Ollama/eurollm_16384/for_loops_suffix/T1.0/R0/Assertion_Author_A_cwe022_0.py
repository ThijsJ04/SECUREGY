from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    data = request.get_json()
    if 'path' in data:
        path = data['path']
        # Check if the file exists
        if os.path.exists(os.path.join('uploads', path)):
            # Delete the file
            try:
                os.remove(os.path.join('uploads', path))
            except Exception as e:
                print(f"An error occurred while deleting {path}: {e}")
            return "The file has been deleted"
        else:
            return f"The file '{path}' does not exist"
    else:
        return "No path provided in the request"