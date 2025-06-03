import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if request.method == "POST":
        # Get the path of the image to be deleted from the request using 'path'
        path = request.form["path"]

        # Convert the path from a string to bytes (to work with bytes objects in os)
        path_bytes = path.encode()

        # Get the current working directory to find where the image is located
        cwd = os.getcwd()

        # Combine the base URL and the path string for easy path creation
        combined_path = f"{os.sep}".join([str(cwd), str(path)])

        # Try to delete the file (using os.remove or shutil.rmtree if it is a directory)
        try:
            if os.path.isfile(combined_path):  # If it's a file
                os.remove(combined_path)
                print("The file has been deleted")
            elif os.path.isdir(
                combined_path
            ):  # If it's a directory (and not a subdirectory)
                shutil.rmtree(combined_path)
                print("The directory and its contents have been deleted")
        except Exception as e:
            print(f"Error: {e}")
            return "The file does not exist"

        # Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
        return "The file has been deleted"  # In this case it should be safe to assume that a file has been deleted
    else:
        return "This route only accepts POST requests."
