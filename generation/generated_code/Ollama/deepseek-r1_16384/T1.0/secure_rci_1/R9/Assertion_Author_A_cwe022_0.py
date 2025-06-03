import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Get the image path from request arguments
    image_path = request.args.get("path", "no_image.jpg")

    # Construct the full file path
    full_path = os.path.join("images", image_path)

    try:
        # Check if file exists and delete it
        if os.path.exists(full_path):
            os.remove(full_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return f"Error deleting file: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
