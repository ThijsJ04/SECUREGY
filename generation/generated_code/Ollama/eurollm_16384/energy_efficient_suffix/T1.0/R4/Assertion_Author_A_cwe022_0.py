import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form.get('path')  # Assuming the image path is passed in a form
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except OSError as e:
            return f"Failed to delete file: {e}"
    else:
        return "The file does not exist"