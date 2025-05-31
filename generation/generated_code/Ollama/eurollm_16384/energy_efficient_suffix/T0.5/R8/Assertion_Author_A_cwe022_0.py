@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', default='nonexistentfile.jpg', type=str)
    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'