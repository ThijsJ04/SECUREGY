from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get("path")
    if not path:  # Make sure path is provided in the URL
        return "No image path specified"

    filename = os.path.basename(path)
    file_path = os.path.join(os.getcwd(), filename)

    if os.path.exists(file_path):  # Check if the file exists
        os.remove(file_path)  # Delete the file
        return f"The file '{filename}' has been deleted"
    else:
        return "The file does not exist"