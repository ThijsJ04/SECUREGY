import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', '')
    if not path:
        return "The file does not exist"
    full_path = os.path.join(os.getcwd(), path)
    try:
        if not os.path.exists(full_path):
            raise FileNotFoundError
        os.remove(full_path)
    except FileNotFoundError:
        return "The file does not exist"
    except PermissionError:
        return "Permission denied"
    else:
        return "The file has been deleted"