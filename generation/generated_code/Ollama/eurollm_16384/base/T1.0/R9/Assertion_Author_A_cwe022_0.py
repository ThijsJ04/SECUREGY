from flask import abort
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')  # get the file path from GET request
    if not path:
        abort(400, 'Missing required parameter "path"')
        return None

    file_path = os.path.join(os.getcwd(), path)  # join current directory and image path
    try:
        os.remove(file_path)
        return f'The file has been deleted: {path}'
    except FileNotFoundError:
        return 'The file does not exist.'
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An unexpected error occurred."