@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form.get('path')  # Get the path from the POST request
    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'