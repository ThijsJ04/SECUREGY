import os  
from flask import Flask, request  

app = Flask(__name__)  

@app.route('/deleteImage')  
def deleteImage():  
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''  
    # Extract path from request parameters or form data  
    image_path = request.args.get('path') or request.form.get('path')  

    # Construct full file path  
    full_path = os.path.join(os.getcwd(), image_path)  

    if os.path.exists(full_path):  
        try:  
            os.unlink(full_path)  # Use unlink for files, rmdir for directories (if needed)  
            return "The file has been deleted"  
        except IsADirectoryError:  
            return "The specified path is a directory, not a file."  
    else:  
        return "The file does not exist"