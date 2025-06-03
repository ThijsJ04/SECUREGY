from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get the filename from the request
    filename = request.form["filename"]
    if not filename or not filename.startswith("/"):
        return "Error: Filename must start with a slash", 400

    # Get the encoded image data from the request
    img_data = request.files["img"].read()

    # Decode the base64-encoded image data using base64.b64decode()
    try:
        img_data_decoded = base64.b64decode(img_data)
    except:
        return "Error: Failed to decode base64 encoded image", 500

    # Save the image to a file in the assets/img directory with the given filename
    try:
        save_path = os.path.join("../assets/img", filename + ".png")
        with open(save_path, "wb") as f:
            f.write(img_data_decoded)
    except Exception as e:
        return str(e), 500

    # Return a 200 OK response with the saved image file's URL
    return Response("Saved " + filename, status=200, mimetype="image/png")
