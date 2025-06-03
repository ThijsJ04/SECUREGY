from flask import request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def delete_image():
    """
    Delete the file specified in the POST request if it exists.
    """
    path = request.form.get(
        "path"
    )  # Get the path of the image to be deleted from the request
    try:
        os.remove(path)  # Attempt to remove the file
        return "The file has been deleted"
    except FileNotFoundError:
        return "The file does not exist"
    except Exception as e:
        print(e)
        return "An error occurred while trying to delete the file"
