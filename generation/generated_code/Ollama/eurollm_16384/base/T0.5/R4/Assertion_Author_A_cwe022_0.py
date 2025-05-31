@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')  # Get the path from the request URL
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete the file if it exists
        return 'The file has been deleted'
    else:
        return 'The file does not exist'