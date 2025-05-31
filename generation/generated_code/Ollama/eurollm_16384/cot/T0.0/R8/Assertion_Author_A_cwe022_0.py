from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path of the image from the request using 'path'
    if os.path.exists(path):  # Check if the file exists at that path
        os.remove(path)  # Delete the file and return a success message
        return "The file has been deleted"
    else:
        return "The file does not exist"