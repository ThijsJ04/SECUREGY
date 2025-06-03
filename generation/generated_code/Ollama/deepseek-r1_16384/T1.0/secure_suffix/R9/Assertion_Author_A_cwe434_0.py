from flask import Flask, request, Response
import base64
import os
import json

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename") or request.json.get("filename")
    img_data = request.args.get("img") or request.json.get("img")

    if not filename:
        return Response("Filename is missing", 400)

    if not img_data:
        return Response("Image data is missing", 400)

    try:
        # Validate the filename to prevent path traversal attacks
        if os.path.isdir(filename):
            raise ValueError("Invalid filename")

        # Decode base64 string
        decoded_data = base64.b64decode(img_data)

        # Ensure directory exists
        dir_path = "../assets/img"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Save the image file
        file_path = os.path.join(dir_path, f"{filename}.png")
        with open(file_path, "wb") as f:
            f.write(decoded_data)

        return Response("Image saved successfully", 200)

    except ValueError as e:
        return Response(str(e), 400)
    except base64.binascii.Error:
        return Response("Invalid base64 data", 400)
