from flask import request

@app.route('/deleteImage')
def deleteImage():
    imagePath = request.path
    # Continue implementation from here