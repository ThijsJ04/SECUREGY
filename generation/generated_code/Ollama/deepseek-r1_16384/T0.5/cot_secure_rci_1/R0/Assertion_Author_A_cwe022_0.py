import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    # Extract path parameter from request
    path = request.args.get("path")

    # Construct full file path using os.path to handle paths correctly
    full_path = os.path.join(os.path.abspath("."), path)

    # Check if the file exists and delete it if it does
    if os.path.exists(full_path):
        os.remove(full_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"


# To run the Flask app, you would typically use something like:
# if __name__ == '__main__':
#     app.run(debug=True)
