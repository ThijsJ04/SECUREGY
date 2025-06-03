from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the filename and img data from the request
    filename = (
        request.args.get("filename") or "unknown"
    )  # If not provided, default to "unknown"
    temp_file = request.files[
        "img"
    ]  # Assuming "img" is the key for the image file in the request form data

    if filename:
        response = Response(temp_file, mimetype="image/png")
    else:
        return "Please provide a filename", 400

    # Save the image to a temporary file
    temp_file.save("../assets/img/{}.png".format(filename))

    # Remove the temporary file after saving it
    os.remove("../assets/img/{}.png".format(filename))

    return response
