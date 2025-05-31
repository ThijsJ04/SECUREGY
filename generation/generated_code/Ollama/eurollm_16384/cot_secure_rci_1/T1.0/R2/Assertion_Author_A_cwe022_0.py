from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')  # Get the file path from query parameter 'path'

    if not os.path.exists(path):
        return "The file does not exist"

    if os.path.isfile(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except OSError as e:
            return f"An error occurred while deleting the file: {e}"
    else:
        return "This is not a valid file path"