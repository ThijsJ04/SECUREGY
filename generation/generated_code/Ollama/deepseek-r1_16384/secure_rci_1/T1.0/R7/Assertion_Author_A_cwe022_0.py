import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')
    if os.path.exists(path):
        try:
            os.remove(path)
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"

if __name__ == '__main__':
    app.run(debug=True)