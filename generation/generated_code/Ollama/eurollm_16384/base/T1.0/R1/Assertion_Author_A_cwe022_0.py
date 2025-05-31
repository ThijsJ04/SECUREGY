import os
from flask import request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'