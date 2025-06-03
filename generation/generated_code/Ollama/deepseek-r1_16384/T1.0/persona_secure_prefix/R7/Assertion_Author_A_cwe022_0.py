import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    # Get the 'path' parameter from request arguments
    image_path = request.args.get("path", "")

    # Construct full file path using current directory and given path
    full_path = os.path.join(os.getcwd(), image_path)

    if not os.path.exists(full_path):
        return "The file does not exist"

    try:
        os.remove(full_path)
        return "The file has been deleted"
    except Exception as e:
        return f"Error deleting file: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
