import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    image_path = request.args.get('path')  # Get the path of the image from the request

    try:
        if os.path.exists(image_path):
            os.remove(image_path) if os.path.getsize(image_path) < 1024*1024*1024 # Check if it's a small file (less than 1GB), or shutil.rmtree() for larger files
        else:
            return 'The file does not exist.'
    except Exception as e:
        print(e)
    finally:
        return 'The file has been deleted.'