@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if request.method == 'POST':
        # Get the path from the POST request
        path = request.form['path']

        # Check if the file exists and is a valid image
        if os.path.isfile(path) and (path.endswith('.jpg') or path.endswith('.jpeg') or path.endswith('.png')):
            # Delete the file
            try:
                os.remove(path)
                print("The file has been deleted")
                return "The file has been deleted"
            except Exception as e:
                print("An error occurred while deleting the file:", str(e))
                return str(e)
        else:
            print("The file does not exist or is not a valid image")
            return "The file does not exist or is not a valid image"
    else:
        print("Invalid request method. Only POST requests are allowed.")
        return "Invalid request method. Only POST requests are allowed."