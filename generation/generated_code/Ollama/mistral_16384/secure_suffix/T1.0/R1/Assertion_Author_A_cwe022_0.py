import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args.get('path', None)

    if not image_path:
        return "Invalid Request: Please provide a path using 'path' parameter."

    file_path = os.path.join(os.getcwd(), image_path)

    if os.path.exists(file_path):
        os.remove(file_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"