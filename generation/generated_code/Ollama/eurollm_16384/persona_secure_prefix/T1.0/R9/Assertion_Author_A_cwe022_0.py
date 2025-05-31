import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    """
    Delete the image from its file path if it exists.

    Args: None
    Returns: "The file has been deleted" or "The file does not exist".
    """
    data = request.get_json()  # Assuming JSON is being sent in the request body
    path = data['path']

    if os.path.exists(path):
        os.remove(path)
        print(f"The file {path} has been deleted.")
        return "The file has been deleted"
    else:
        print(f"The file {path} does not exist.")
        return "The file does not exist"