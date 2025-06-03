from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/deleteImage", methods=["POST"])
def deleteImage():
    if not request.files:
        return "No image data supplied in the request."
    path = os.path.join(os.getcwd(), "uploads", str(request.form["image_filename"]))
    if os.path.exists(path):
        print(
            "Image to be deleted: ", path
        )  # This line is added for debugging purposes only
        if request.method == "DELETE":
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
    else:
        print(
            "The file does not exist"
        )  # This line is added for debugging purposes only
        return "The file does not exist"
