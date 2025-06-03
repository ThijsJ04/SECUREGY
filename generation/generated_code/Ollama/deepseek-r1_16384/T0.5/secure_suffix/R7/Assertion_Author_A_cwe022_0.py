import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if not path:
        return "The file does not exist"

    # Ensure the path is within the current directory to prevent traversal attacks
    full_path = os.path.abspath(os.path.join(os.getcwd(), path))

    if not os.path.exists(full_path):
        return "The file does not exist"

    try:
        os.remove(full_path)
        return "The file has been deleted"
    except Exception as e:
        return f"Error deleting file: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
