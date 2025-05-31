import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):  # check if the file exists
        try:
            os.remove(path)  # delete it from the given path in the current directory
            return "The file has been deleted"
        except Exception as e:
            print("An error occurred while deleting the file:", str(e))
    else:
        return "The file does not exist"