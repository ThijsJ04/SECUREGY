import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract the path parameter from the request
    image_path = request.args.get("path")

    # Check if the file exists before attempting to delete
    if os.path.exists(image_path):
        try:
            # Use os.remove() to delete the file
            os.remove(image_path)
            return "The file has been deleted"
        except Exception as e:
            # Handle any potential errors during deletion (e.g., permission issues, file not found)
            return f"Error deleting file: {str(e)}"
    else:
        # Return message if the file does not exist
        return "The file does not exist"


# To run this Flask application:
# 1. Save it as an .py file
# 2. Open a terminal and navigate to the directory containing the file
# 3. Run: python filename.py
