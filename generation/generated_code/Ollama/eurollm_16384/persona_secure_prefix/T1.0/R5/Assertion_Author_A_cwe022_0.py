@app.route('/deleteImage', methods=['POST'])
def delete_image():
    data = request.get_json()
    if not data or 'path' not in data:
        return "Invalid JSON or missing path", 400

    path = data['path']
    try:
        os.remove(path)
        return f"The file {path} has been deleted"
    except OSError as e:
        # Handle the error, possibly log it, and return a message indicating that the operation failed
        return f"Failed to delete the file {path}: {e}", 500