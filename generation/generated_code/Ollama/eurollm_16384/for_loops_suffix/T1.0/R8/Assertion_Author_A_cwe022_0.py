import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path:
        abort(400, 'Missing required parameter "path"')

    try:
        os.remove(path)
        return f'The file {path} has been deleted'
    except OSError as e:
        return f'An error occurred: {e}. The file does not exist.'