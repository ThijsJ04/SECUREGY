import os
from flask import request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', default='not_found')  # Get the path from the query string or use a default value if not provided
    if os.path.exists(path):
        os.remove(path)  # Remove the file (this will raise an OSError if the file does not exist)
        return "The file has been deleted"
    else:
        return "The file does not exist"