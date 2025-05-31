import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    file_path = request.args.get('path', '')
    if not file_path:
        return "The file does not exist"

    # Check if the file exists and is in the current directory
    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            os.remove(file_path)
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"

if __name__ == "__main__":
    app.run(debug=True)