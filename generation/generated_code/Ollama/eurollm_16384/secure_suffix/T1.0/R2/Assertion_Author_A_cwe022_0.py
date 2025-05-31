import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def delete_image():
    path = request.args.get('path')  # Get the image path from the query string
    if os.path.exists(path):            # Check if the file exists
        os.remove(path)                 # Delete the file
        return f"The file '{path}' has been deleted."
    else:
        return "The file does not exist."