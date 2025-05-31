from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    data = request.form['path']
    if not os.path.exists(data):  # Check if file exists before deletion
        return 'The file does not exist'
    os.remove(data)               # Delete the file
    return 'The file has been deleted'