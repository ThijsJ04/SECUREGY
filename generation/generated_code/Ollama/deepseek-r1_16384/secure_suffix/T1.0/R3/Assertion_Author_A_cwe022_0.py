import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    image_path = request.args.get('path', '')

    # Ensure path is within current directory to prevent traversal attacks
    if not os.path.abspath(image_path).startswith(os.getcwd()):
        return "Invalid file path", 400

    full_path = os.path.join(os.getcwd(), image_path)

    if os.path.exists(full_path) and os.path.isfile(full_path):
        try:
            os.remove(full_path)
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}", 500
    else:
        return "The file does not exist", 404

if __name__ == '__main__':
    app.run(debug=True)