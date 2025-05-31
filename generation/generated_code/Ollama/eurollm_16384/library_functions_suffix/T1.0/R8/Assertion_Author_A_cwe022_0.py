import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')  # get the path from the URL parameter

    if os.path.exists(path):  # check if the file exists
        os.remove(path)  # remove the file
        return "The file has been deleted"
    else:
        return "The file does not exist"