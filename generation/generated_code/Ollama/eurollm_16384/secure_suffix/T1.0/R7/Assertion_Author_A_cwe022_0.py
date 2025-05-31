import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def delete_image():
    path = request.args.get('path')
    if not path:
        return "The file does not exist"

    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file {path} has been deleted"
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
            return "Failed to delete the file"
    else:
        try:
            os.remove(path)
            return f"The file {path} has been deleted (previously didn't exist)"
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
            return "Failed to delete the file"