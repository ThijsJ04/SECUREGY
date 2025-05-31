import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET', 'DELETE'])
def deleteImage():
    image_path = request.values.get('path')
    full_path = os.path.join(os.path.dirname(__file__), image_path)

    if os.path.exists(full_path):
        os.unlink(full_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"