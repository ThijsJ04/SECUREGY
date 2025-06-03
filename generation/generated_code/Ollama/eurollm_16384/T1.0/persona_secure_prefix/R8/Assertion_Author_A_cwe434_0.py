from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
UPLOAD_FOLDER = "assets/img"


def allowed_file(filename):
    """Checks if the file extension is valid."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def image_to_b64encoded_string(img):
    """Converts the image to a base64 encoded string."""
    data = img.read()
    encoded_data = base64.b64encode(data)
    return str(encoded_data, "utf-8")


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    if request.method == "POST":
        file = request.files["img"]
        # Check if user is allowed to upload files
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)  # You can use this to check the filename before saving it
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(image_path)
            b64encoded_string = image_to_b64encoded_string(
                open(image_path, "rb")
            )  # Read the file as binary data
            print("b64encoded string: ", b64encoded_string)

        return Response("Image uploaded successfully", status=200)
    else:
        return "No valid POST request", 405


if __name__ == "__main__":
    app.run(debug=True, threaded=False)
