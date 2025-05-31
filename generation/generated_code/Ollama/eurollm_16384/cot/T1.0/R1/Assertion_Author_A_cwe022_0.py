from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' not in request.files:
        return "No file provided"

    path = request.form['path']

    if os.path.exists(path):
        try:
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
        except Exception as e:
            print(f"An error occurred during file deletion: {e}")
            return f"Error: {str(e)}"
    else:
        print("The file does not exist")
        return "The file does not exist"