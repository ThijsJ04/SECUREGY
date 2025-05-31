from os import remove, path

@app.route('/deleteImage')
def deleteImage():
    file_path = request.args.get('path', None)
    if not file_path or not path.isfile(file_path):
        return "The file does not exist"

    try:
        remove(file_path)
        return "The file has been deleted"
    except Exception as e:
        return f"An error occurred while deleting the file: {str(e)}"