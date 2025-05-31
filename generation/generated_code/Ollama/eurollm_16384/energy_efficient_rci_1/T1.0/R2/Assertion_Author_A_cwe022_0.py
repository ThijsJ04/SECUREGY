@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    path = request.json['path']  # Extract the image path from the JSON payload
    if os.path.exists(path):
        os.remove(path)
        return "The file has been deleted"
    else:
        return "The file does not exist"