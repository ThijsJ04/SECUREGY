@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path from the form data
    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'