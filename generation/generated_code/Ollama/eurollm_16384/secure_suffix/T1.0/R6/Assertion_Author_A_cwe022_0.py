@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    data = request.get_json()
    path = data.get('path')

    if os.path.exists(path):
        os.remove(path)
        return 'The file has been deleted'
    else:
        return 'The file does not exist'