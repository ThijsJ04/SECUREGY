import os
from flask import request

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    path = request.json.get('path')
    if path and os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"