import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")  # Get 'path' from query parameters
    full_path = os.path.join(os.getcwd(), path)  # Construct absolute path

    if os.path.exists(full_path):
        try:
            os.remove(full_path)  # Delete the file
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"
