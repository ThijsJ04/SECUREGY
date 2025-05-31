import os
from flask import request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path from form data
    if not os.path.exists(path):
        return 'The file does not exist.'
    os.remove(path)
    return f"The file has been deleted."