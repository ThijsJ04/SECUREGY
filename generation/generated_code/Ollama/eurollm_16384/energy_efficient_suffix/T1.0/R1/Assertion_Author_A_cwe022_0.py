from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage')
def delete_image():
    path = request.args.get('path')  # Assuming the 'path' is in the query string like '?path=example.jpg'
    if os.path.exists(path):  # Check if file exists at given path
        os.remove(path)  # Delete file
        print("The file has been deleted")
        return "The file has been deleted"
    else:
        return "The file does not exist"