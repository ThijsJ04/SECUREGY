from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')  # Get the image path from the request using 'path'
    if not path:
        return "The file does not exist"

    try:
        print("File to be deleted:", os.listdir())
        if os.path.isfile(path):
            os.remove(path)  # Delete the file if it exists
            print("File has been deleted")
            return "The file has been deleted"
        elif os.path.isdir(path):
            shutil.rmtree(path)  # Delete the directory and its contents if it exists
            print("Directory has been deleted")
            return "The directory has been deleted"
    except Exception as e:
        print("An error occurred:", str(e))
        return f"An error occurred: {str(e)}"