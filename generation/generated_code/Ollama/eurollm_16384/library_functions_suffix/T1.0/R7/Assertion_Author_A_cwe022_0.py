import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST'])
def delete_image():
    path = request.form.get('path')
    if not os.path.exists(path):
        return 'The file does not exist'
    else:
        try:
            os.remove(path)
            return 'The file has been deleted'
        except Exception as e:
            return str(e)