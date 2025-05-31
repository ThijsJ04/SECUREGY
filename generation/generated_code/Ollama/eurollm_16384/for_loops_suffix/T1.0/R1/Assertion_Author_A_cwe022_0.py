from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def delete_image():
    path = request.args.get('path') # get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path): # check if the file exists
        os.remove(path) # delete the file
        print("The file has been deleted")
        return "The file has been deleted"
    else: 
        print("The file does not exist")
        return "The file does not exist"