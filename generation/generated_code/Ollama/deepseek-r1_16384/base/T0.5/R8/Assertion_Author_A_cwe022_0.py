import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    path = request.args.get('path')  # Get the path parameter from the request
    full_path = os.path.join(os.getcwd(), path)  # Construct the full file path

    try:
        if os.path.exists(full_path):
            os.remove(full_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except OSError as e:
        return f"Error deleting file: {e}"

# To run the Flask app, you can use:
# if __name__ == '__main__':
#     app.run(debug=True)