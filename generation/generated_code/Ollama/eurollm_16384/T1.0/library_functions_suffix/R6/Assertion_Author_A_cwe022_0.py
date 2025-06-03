import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    try:
        if request.method == "POST":
            # Get the file path from the POST request data
            path = request.form["path"]

            # Make sure to keep the code inside the if statement
            # so that the error message can be written there in case of failure.
        else:
            abort(405)  # Method Not Allowed
    except Exception as e:
        abort(500, str(e))

    if os.path.exists(path):
        try:
            # Use the safe_remove() function from the shutil module to delete the file safely
            shutil.safe_remove(path)
        except Exception as e:
            # If the file cannot be deleted, write an error message
            abort(501, str(e))
    else:
        abort(404, "The file does not exist")  # 404 File Not Found
