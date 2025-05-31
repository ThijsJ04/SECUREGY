import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', type=str)
    if os.path.exists(path):
        try:
            os.remove(path)
            return 'The file has been deleted'
        except Exception as e:
            print("Error occurred while deleting the file")
            return str(e)
    else:
        return "The file does not exist"