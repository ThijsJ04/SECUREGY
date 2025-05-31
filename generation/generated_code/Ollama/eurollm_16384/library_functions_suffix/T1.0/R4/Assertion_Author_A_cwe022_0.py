from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path:
        return 'The file does not exist'

    try:
        target_dir = os.path.dirname(path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)
        file_to_delete = path
        os.remove(path)
        print('The file has been deleted')
        return 'The file has been deleted'
    except Exception as e:
        return str(e)