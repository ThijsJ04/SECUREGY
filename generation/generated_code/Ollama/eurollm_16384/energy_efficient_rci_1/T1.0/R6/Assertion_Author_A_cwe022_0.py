from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path_from_request = request.form.get('path')  # Get the file path from the POST request
    if os.path.exists(path_from_request):
        os.remove(path_from_request)  # Delete the file if it exists
        return "The file has been deleted"
    else:
        return "The file does not exist"