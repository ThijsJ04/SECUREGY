import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def delete_image():
    path = request.args.get('path')
    if not path:
        return 'The file does not exist.'

    # Check if the file exists at the given path
    file_exists = os.path.isfile(path)

    # Delete the file if it exists
    if file_exists:
        try:
            os.remove(path)
        except OSError as e:
            print(f"Error deleting file: {e}")
            return f"The file has been deleted, but an error occurred."

        # Return a success message if the file was successfully deleted
        return 'The file has been deleted.'
    else:
        return 'The file does not exist.'