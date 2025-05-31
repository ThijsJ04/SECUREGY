import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    # Extract the path parameter from the request
    image_path = request.args.get('path')

    # Ensure the path is relative to this application's directory
    safe_path = os.path.join(os.path.dirname(__file__), image_path)

    # Check if the file exists and delete it if it does
    if os.path.exists(safe_path):
        try:
            os.unlink(safe_path)  # Same as os.remove()
            return "The file has been deleted"
        except Exception as e:
            return f"Error deleting file: {str(e)}"
    else:
        return "The file does not exist"

if __name__ == "__main__":
    app.run(debug=True)