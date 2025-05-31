import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    """Delete the image from the given path in the current directory if it exists."""
    data = request.get_json()
    path = data.get('path')

    if path:
        # Check if the file exists and is a valid image
        try:
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
        except FileNotFoundError:
            return "The file does not exist"
        except OSError as e:
            return f"An error occurred: {e}"
    else:
        return "No path provided"