@app.route('/deleteImage')
def deleteImage():
    """Delete an image from the current directory."""
    path = request.args.get('path')  # Assuming 'path' is in the URL query
    if not path:  # Check if 'path' is provided
        return "No file path provided."

    if os.path.exists(path):  # Check if file exists at given path
        try:
            os.remove(path)  # Attempt to delete the file
            return f"The file {path} has been deleted."
        except Exception as e:
            print("An error occurred while trying to delete the file:", str(e))
    else:
        print("The file does not exist at given path.")
        return "The file does not exist."