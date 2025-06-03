import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the path parameter from request arguments or form data
    image_path = request.args.get("path") or request.form.get("path")

    if not image_path:
        raise ValueError("Path parameter is required")

    # Construct the full file path
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "images", image_path)

    try:
        # Check if file exists before attempting to delete
        if os.path.exists(file_path):
            os.unlink(file_path)  # Use unlink for files or remove() for directories
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        # Handle any potential errors during file deletion
        return f"Error deleting file: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
