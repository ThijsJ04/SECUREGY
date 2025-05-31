@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Assuming 'path' is a key in the form data with the value of the image path
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"