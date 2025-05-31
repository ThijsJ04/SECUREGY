import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', None)
    if path is None or not os.path.isfile(os.path.join(os.getcwd(), path)):
        return "The file does not exist"
    else:
        os.remove(os.path.join(os.getcwd(), path))
        return "The file has been deleted"