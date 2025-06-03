import base64
from werkzeug.utils import secure_filename
from flask import Flask, request, File, Response
import os

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/img/upload", methods=["POST"])
def upload_img():
    print(
        "File being uploaded: ", request.files
    )  # This line is not needed but it is helpful to know what kind of files are being uploaded

    if "file" in request.files and request.files["file"].filename != "":
        filename = secure_filename(
            request.form["filename"]
        )  # Assuming "filename" comes from form data
        base64_data = request.files[
            "img"
        ]  # Assuming "img" comes from the file-like request object, not a string encoded with base64
        decoded_file_bytes = base64.b64decode(base64_data)

        if allowed_file(filename):
            full_path = os.path.join(
                app.config["UPLOAD_FOLDER"], filename
            )  # Assuming the upload folder is specified in app.config, e.g., "./static/img" by default
            print(
                "Creating a new file..."
            )  # This line can be helpful to track progress
            with open(full_path, "wb") as f:
                f.write(decoded_file_bytes)
        else:
            return "Unsupported File Type", 403
    else:
        return "No file part in request", 400
    print("File saved to folder...")  # This line can be helpful to track progress
    return "File Saved Successfully"
