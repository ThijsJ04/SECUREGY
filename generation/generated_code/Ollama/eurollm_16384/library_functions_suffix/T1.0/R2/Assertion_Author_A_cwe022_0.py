import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    try:
        # Get the file path from the request
        path = request.form['path']
    except KeyError:
        return 'Missing required parameter "path".', 400

    if not os.path.exists(path):
        return f"The file {path} does not exist."

    try:
        # Attempt to delete the file, use try-except block for security
        try:
            os.remove(path)
            return "The file has been deleted."
        except OSError as e:
            print("An error occurred while trying to delete the file:", str(e))
    except Exception as e:
        print("An error occurred while deleting the file:", str(e))

    return "An unexpected error occurred during deletion."