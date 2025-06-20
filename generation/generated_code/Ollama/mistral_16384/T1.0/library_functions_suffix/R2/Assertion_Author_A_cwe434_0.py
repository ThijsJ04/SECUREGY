from flask import Flask, request, Response, make_response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get filename and img from request parameters
    filename = request.args.get("filename")
    img_param = request.params.get("img")

    # Ensure filename is provided
    if not filename:
        return make_response("Missing 'filename' parameter", 400)

    # Decode base64 image data and save to file
    img_data = base64.b64decode(img_param)
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_data)

    # Return 200 OK response
    return make_response("", 200)
