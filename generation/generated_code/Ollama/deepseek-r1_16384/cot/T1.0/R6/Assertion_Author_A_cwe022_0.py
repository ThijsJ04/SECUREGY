import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', '')
    if not path or not os.path.isfile(path):
        return "The file does not exist"
    try:
        os.remove(path)
        return "The file has been deleted"
    except Exception as e:
        return f"Error deleting file: {e}"

app.run()