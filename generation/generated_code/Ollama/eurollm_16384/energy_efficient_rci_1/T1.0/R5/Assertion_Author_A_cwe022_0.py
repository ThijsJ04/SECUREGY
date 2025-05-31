@app.route('/deleteImage', methods=['POST'])
def delete_image():
    path = request.form['path']  # Assuming the image path is passed in the form data as 'path' key
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"