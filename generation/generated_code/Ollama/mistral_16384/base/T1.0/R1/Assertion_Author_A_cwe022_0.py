import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', None)
    if not path or not os.path.exists(os.path.join(os.getcwd(), path)):
        return "The file does not exist"

    try:
        os.remove(os.path.join(os.getcwd(), path))
        return "The file has been deleted"
    except Exception as e:
        return f"Error occurred while deleting the file: {e}"