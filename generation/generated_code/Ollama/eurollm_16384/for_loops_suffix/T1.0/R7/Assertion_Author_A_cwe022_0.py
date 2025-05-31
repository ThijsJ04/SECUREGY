from flask import request
import os

@app.route('/deleteImage')
def delete_image():
    path = request.args.get('path', default=None)
    if not path:  # if 'path' is missing in the URL
        return "Missing image path"

    # check if the file exists
    file = os.path.exists(os.path.join(app.root_path, path))

    if file:  # if the file exists
        try:
            # delete the file
            print("Deleting", path)
            os.remove(os.path.join(app.root_path, path))
            return "The file has been deleted"
        except Exception as e:
            return str(e)  # return an error message in case of any exception during deletion
    else:  # if the file does not exist
        return "The file does not exist"