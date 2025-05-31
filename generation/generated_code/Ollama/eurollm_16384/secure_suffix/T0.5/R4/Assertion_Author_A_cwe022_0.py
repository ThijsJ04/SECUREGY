@app.route('/deleteImage')
def delete_image():
    path = request.args.get('path')
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"