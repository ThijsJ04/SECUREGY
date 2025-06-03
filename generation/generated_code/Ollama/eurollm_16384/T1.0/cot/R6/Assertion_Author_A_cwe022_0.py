from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage")
def delete_image():
    path = request.args.get(
        "path", default="image.jpg"
    )  # default image filename in case none is provided
    if not path:
        return "The file does not exist"

    # Check if the directory exists where the file is located and if the file actually exists
    dir_path = os.path.dirname(
        __file__
    )  # Get the directory of this script to know where the file should be deleted
    dir_path = os.path.join(dir_path, "image_folder")  # Create a folder for image files
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)  # Create the directory if it doesn't exist
    path = os.path.join(
        dir_path, path
    )  # join path with dir so that you can delete in the right folder

    if not os.path.exists(path):
        return "The file does not exist"

    try:
        os.remove(path)  # Try to delete the file
        return "The file has been deleted"
    except (
        OSError
    ) as e:  # Handle any exception that occurs when trying to remove the file
        return str(e)
