from flask import Flask, request, Response
import base64
import os
import re

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get filename and img parameters from request
    filename = request.args.get("filename", "")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response(status=400)

    # Sanitize the filename to prevent directory traversal attacks
    allowed_chars = re.compile(r"^[\w-]+$")
    clean_filename = allowed_chars.sub("", filename)

    if not clean_filename:
        return Response(status=400)

    # Add .png extension
    clean_filename += ".png"

    # Create the directory if it doesn't exist
    os.makedirs("../assets/img", exist_ok=True)

    # Save the image data
    file_path = f"../assets/img/{clean_filename}"
    with open(file_path, "wb") as f:
        try:
            decoded_data = base64.b64decode(img_data)
            f.write(decoded_data)
        except Exception as e:
            return Response(status=500)

    return Response(status=200)
