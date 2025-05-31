from os import remove, path

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    path_to_delete = request.args.get('path')
    if path.exists(path_to_delete) and path.isfile(path_to_delete):
        remove(path_to_delete)
        return "The file has been deleted"
    else:
        return "The file does not exist"