import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not os.path.exists(path):
        return 'The file does not exist'
    os.remove(path)
    return 'The file has been deleted'