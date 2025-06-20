import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    """
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    """
    try:
        # Get the path parameter from the request
        image_path = request.args.get("path")

        # Construct the full file path
        full_path = os.path.join(os.getcwd(), image_path)

        if os.path.exists(full_path):
            os.remove(full_path)  # Delete the file
            return jsonify(
                {"message": "The file has been deleted", "status": "success"}
            ), 200
        else:
            return jsonify(
                {"message": "The file does not exist", "status": "error"}
            ), 404
    except OSError as e:
        return jsonify(
            {"message": f"Error deleting file: {str(e)}", "status": "error"}
        ), 500


if __name__ == "__main__":
    app.run(debug=True)
