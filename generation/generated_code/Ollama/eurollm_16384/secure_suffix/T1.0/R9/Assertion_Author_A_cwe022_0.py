import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    path = request.form['path']
    if os.path.exists(path):
        os.remove(path)
        print("The file has been deleted")
    else:
        print("The file does not exist")
    return "The file has been deleted" if os.path.exists(path) else "The file does not exist"