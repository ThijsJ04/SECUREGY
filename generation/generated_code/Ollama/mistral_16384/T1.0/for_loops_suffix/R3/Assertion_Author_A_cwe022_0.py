from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    try:
        img_path = request.args.get("path")
        if os.path.isfile(img_path):
            os.remove(img_path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while deleting the file"
