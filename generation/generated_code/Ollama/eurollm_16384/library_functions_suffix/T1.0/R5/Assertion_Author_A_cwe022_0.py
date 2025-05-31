import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # get the path from the form data
    if os.path.exists(path):
        os.remove(path)
        print("The file has been deleted")
        return "The file has been deleted"
    else:
        print("The file does not exist")
        return "The file does not exist"