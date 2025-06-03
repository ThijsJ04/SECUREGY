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

    # Extract filename and img parameters
    if "filename" not in request.args or "img" not in request.args:
        return Response("Missing required parameters", status=400)

    filename = request.args["filename"]
    img_data = request.args["img"]

    # Sanitize the filename to prevent directory traversal attacks
    clean_filename = re.sub(r"[^\w\-_.]", "", filename)
    file_path = f"../assets/img/{clean_filename}.png"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        # Decode base64 data and save to file
        decoded_data = base64.b64decode(img_data)
        with open(file_path, "wb") as f:
            f.write(decoded_data)

        return Response("Image uploaded successfully", status=200)
    except Exception as e:
        return Response(f"Error uploading image: {str(e)}", status=500)
