from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    try:
        image_path = request.args.get('path')  # get the path of the image from the query string parameter 'path'
        delete_path = os.path.join(os.getcwd(), image_path)  # join the current working directory with the image path
        if os.path.exists(delete_path):
            os.remove(delete_path)  # delete the file if it exists
            return 'The file has been deleted'
        else:
            return 'The file does not exist'
    except Exception as e:
        return f'Error: {str(e)}'