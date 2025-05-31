from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def delete_image():
    try:
        path = request.args.get('path')  # Assuming 'path' is a query parameter with the file path
        if os.path.exists(path):
            os.remove(path)
            print("The file has been deleted")
    except FileNotFoundError:
        print("The file does not exist")

    return "The file has been deleted" if os.path.exists(path) else "The file does not exist"