import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        path = request.form.get('path')  # Assuming the image file path is in a form field named 'path'
        filename = os.path.basename(path)
        print("File:", filename, "is being deleted.")
    else:
        return "Method Not Allowed"

    if os.path.exists(path):  # Check if the file exists before deletion
        os.remove(path)
        response = {'status': 'success', 'message': f'The file {filename} has been deleted'}
    else:
        response = {'status': 'failure', 'message': f'The file {filename} does not exist'}
        print("File does not exist")

    return response, 200