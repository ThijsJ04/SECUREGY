import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args.get('path')
    if os.path.isfile(os.path.join(os.getcwd(), image_path)):
        os.remove(os.path.join(os.getcwd(), image_path))
        return "The file has been deleted"
    else:
        return "The file does not exist"