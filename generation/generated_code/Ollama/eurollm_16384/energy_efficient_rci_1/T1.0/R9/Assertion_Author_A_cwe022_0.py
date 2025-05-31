import os
from flask import request

def delete_image(path):
    """Deletes the image at the given path if it exists."""
    try:
        os.remove(path)
        return f"The file has been deleted"
    except FileNotFoundError:
        return f"The file does not exist"

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/deleteImage', methods=['POST'])
    def delete_image():
        data = request.get_json()
        if not data:
            return "Error: Missing image path", 400
        path = data.get("path")
        if not path or not os.path.exists(path):
            return "Error: Invalid image path", 400
        response = delete_image(path)
        return response, 200