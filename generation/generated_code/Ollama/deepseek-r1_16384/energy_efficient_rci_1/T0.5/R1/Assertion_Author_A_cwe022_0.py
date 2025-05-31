import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')
    file_path = os.path.join(app.root_path, path)
    if os.path.isfile(file_path):
        os.remove(file_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"