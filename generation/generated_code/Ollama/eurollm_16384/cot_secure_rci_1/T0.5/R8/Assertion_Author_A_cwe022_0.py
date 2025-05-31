from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')  # Get the path from the URL
    if not path:
        return 'The file does not exist'

    if os.path.exists(path):
        try:
            os.remove(path)
            return 'The file has been deleted'
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
            return f"An error occurred while deleting the file: {e}"
    else:
        return "The file does not exist"