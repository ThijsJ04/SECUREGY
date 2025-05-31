from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path:  # Check if the file path is provided in the URL query parameter
        return "Missing file path", 400
    abs_path = os.path.join(__file__, '', path)
    if not os.path.exists(abs_path):
        return f"The file {abs_path} does not exist."
    if not os.access(abs_path, os.F_OK | os.R_OK | os.W_OK):
        return "Permission denied."
    os.remove(abs_path)  # Attempt to delete the file
    return f"The file {abs_path} has been deleted."