@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.form['path']  # Get the path of the image to be deleted from the request using 'path'
    if os.path.exists(path):
        os.remove(path)
        print("The file has been deleted")
        return "The file has been deleted"
    else:
        print("The file does not exist")
        return "The file does not exist"