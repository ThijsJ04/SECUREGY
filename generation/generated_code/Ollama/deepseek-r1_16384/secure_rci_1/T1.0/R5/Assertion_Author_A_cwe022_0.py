import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args.get('path', '')
    current_dir = os.path.abspath('.')
    full_path = os.path.join(current_dir, image_path)

    if os.path.exists(full_path):
        os.remove(full_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"