import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    image_path = request.args.get('path')

    if image_path and os.path.exists(image_path):
        os.remove(image_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"