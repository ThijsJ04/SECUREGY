import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path_to_image = request.form['path']  # Assuming the image path is passed in a form as 'path'
    if os.path.exists(path_to_image):
        os.remove(path_to_image)
        return "The file has been deleted"
    else:
        return "The file does not exist"