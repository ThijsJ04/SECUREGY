@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path')
    if path and os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'