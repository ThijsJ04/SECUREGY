import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', '')
    file_path = os.path.join(os.getcwd(), path)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except FileNotFoundError:
        return "The file does not exist"
    except PermissionError:
        return "Permission denied to delete the file"
    except Exception as e:
        return f"An error occurred while deleting the file: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)