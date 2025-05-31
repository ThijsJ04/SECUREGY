@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', default='nonexistent_file.jpg')
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"