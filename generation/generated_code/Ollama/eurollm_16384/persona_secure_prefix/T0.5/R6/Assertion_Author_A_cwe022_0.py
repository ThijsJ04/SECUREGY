@app.route('/deleteImage')
def deleteImage():
    path = request.args.get('path', default='nonexistent_image.jpg')
    if os.path.exists(os.path.join(os.getcwd(), path)):
        os.remove(os.path.join(os.getcwd(), path))
        return 'The file has been deleted'
    else:
        return 'The file does not exist'