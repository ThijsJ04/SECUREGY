import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args.get('path')  # Get path from query parameters
    current_dir = os.path.abspath(os.curdir)  # Get current directory
    image_full_path = os.path.join(current_dir, image_path)  # Construct full file path

    if os.path.exists(image_full_path):
        try:
            os.unlink(image_full_path)  # Delete the file
            return "The file has been deleted"
        except OSError as e:
            return f"Error deleting file: {e}"
    else:
        return "The file does not exist"

if __name__ == '__main__':
    app.run()