import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    try:
        # Get the file name from the request parameters
        path = request.args.get("path")
    except Exception as e:
        return "Error parsing request. Error: {}".format(e)

    # Construct the full file path and check if it exists
    try:
        full_path = os.path.join(os.getcwd(), path)
        print(os.path.exists(full_path))
        if os.path.exists(full_path):
            # Delete the file
            print("Deleting file: {}".format(full_path))
            os.remove(full_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        print(
            "Error checking if the file exists or deleting the file. Error: {}".format(
                e
            )
        )
        return "The file does not exist or could not be deleted."
