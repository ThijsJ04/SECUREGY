from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


# Function to save an image to disk
def save_image(filename):
    if not filename.startswith("../assets/img/"):
        return "Error: Invalid file path"
    asset_path = os.path.join("..", "assets", "img", filename[8:]) + ".png"
    try:
        data = request.files["img"]
        open(asset_path, "wb").write(data)
    except:
        return "Error saving file"
    else:
        os.remove("../assets/temp_file.bin")
        return "File saved successfully"


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Handle the image upload and save it to disk as png.
    :return: a Response with status code equals to 200 if the file is saved successfully, or a custom error message if not.
    """
    filename = request.form["file_name"]
    content_type, _ = request.content_type
    if not content_type:
        return "No file content type detected"

    # Get the base64 encoded data from the image parameter
    encoded_data = request.stream.read()
    decoded_image = base64.b64decode(encoded_data)

    response = Response(save_image(filename), status=200, mimetype="text/plain")
    return response
