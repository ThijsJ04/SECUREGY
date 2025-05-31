@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the image path from the request form data
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete the file if it exists
        return "The file has been deleted"
    else:
        return "The file does not exist"