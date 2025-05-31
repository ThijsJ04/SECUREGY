import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if 'path' not in request.files:
        return "No file provided"
    path = request.form['path']  # Assuming the image path is passed as a form parameter named 'path'
    if os.path.exists(path):
        try:
            os.remove(path)
            return f"The file {path} has been deleted"
        except Exception as e:
            return str(e)  # Return any error message if the deletion fails
    else:
        return "The file does not exist"