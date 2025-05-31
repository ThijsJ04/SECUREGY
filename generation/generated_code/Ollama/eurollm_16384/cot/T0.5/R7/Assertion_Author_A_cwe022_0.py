import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args['image_path']  # Retrieve the image path from the request

    if os.path.exists(image_path):  # Check if the file exists at the specified path
        os.remove(image_path)  # Delete the file (ensure you have necessary permissions)
        return "The file has been deleted"
    else:
        return "The file does not exist"