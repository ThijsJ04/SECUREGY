from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['DELETE'])
def delete_image():
    path = request.args.get('path')
    if not path:
        return 'The file does not exist.'

    try:
        os.remove(path)
        return 'The file has been deleted.'
    except FileNotFoundError:
        return 'The file does not exist.'