from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")  # Get the path of the image from the request
    if not path:
        return "Error: No path provided"

    if os.path.exists(path):
        try:
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
        except Exception as e:
            print("An error occurred during deletion: ", str(e))
            return "Error: An error occurred during deletion"
    else:
        print("The file does not exist")
        return "The file does not exist"
