import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["GET"])
def deleteImage():
    if request.method == "GET":
        # Retrieve the path of the image to be deleted from the request using 'path'
        path = request.args.get(
            "path"
        )  # Assuming that the path is passed as a GET parameter named "path"

        # Check if the file exists in the current directory
        if os.path.exists(path):
            # Delete the file if it exists
            try:
                os.remove(path)
                print("The file has been deleted")
            except Exception as e:
                print(f"An error occurred while trying to delete the file: {e}")
        else:
            print("The file does not exist")
    return "", 204  # No content is sent back, indicating successful deletion
