from flask import request, url_for
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path'. Delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    path = url_for("deleteImage", _external=True)
    print(path)  # prints a URL that corresponds to this route with a 'GET' method

    # Now we get the requested path from the request body (not shown in your code snippet):
    # path = request.form['path'] or None
    if not path:
        return "The file does not exist"
    try:
        print(
            os.remove(path)
        )  # prints either a True or False depending on whether the file was deleted or not
        return "The file has been deleted"
    except Exception as e:
        return f"An error occurred while deleting the file: {e}"
