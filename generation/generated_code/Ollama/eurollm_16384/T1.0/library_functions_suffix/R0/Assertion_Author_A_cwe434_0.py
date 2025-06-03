import base64
from flask import Flask, request, Response
import os

app = Flask(__name__)


# Convert image upload to base64
@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request
    filename = request.form.get("filename")
    if not filename:
        return "Missing required parameter: filename", 400

    # Get the image content from the POST request
    img_content = request.files["img"]
    data = img_content.read()  # assuming img is an uploaded file, read it as bytes

    # Encode the image content into base64 string
    b64str = base64.b64encode(data).decode("utf-8")
    print("Base64 encoded image:", b64str)

    # Create a temporary directory to store the uploaded files
    temp_dir = os.path.join(
        os.getcwd(), "uploads", str(int(time.time() * 1000))
    )  # create a new temp dir each second
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    path = os.path.join(
        temp_dir, filename + ".png"
    )  # save the file with the same name as in the form

    # Save the base64 string to a file (use temp file to avoid problems when running script on production env)
    with open(path, "wb") as f:
        f.write(
            base64.decode(b64str)
        )  # encode and write back into binary data using base64
        print("Saved uploaded image to file", path)

    print("Image saved successfully.")
    return "", 200
