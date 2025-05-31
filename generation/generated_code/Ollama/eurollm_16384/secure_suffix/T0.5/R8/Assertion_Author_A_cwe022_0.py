@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    path = request.args.get('path')
    if not path or not os.path.exists(path):
        return 'The file does not exist'
    os.remove(path)
    return 'The file has been deleted'