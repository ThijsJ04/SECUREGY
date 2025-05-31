import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')
    try:
        if not path or not isinstance(path, str):
            raise FileNotFoundError
        os.remove(path)
        return "The file has been deleted"
    except FileNotFoundError:
        return "The file does not exist"

# Output is as above, no additional text.