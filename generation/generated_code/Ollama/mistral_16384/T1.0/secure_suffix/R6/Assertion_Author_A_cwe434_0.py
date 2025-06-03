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
    filename = request.args.get("filename")
    img_str = request.values.get("img")

    # Decode base64 string into bytes and save as an image file
    img_data = base64.b64decode(img_str)
    img_filepath = os.path.join(
        os.path.dirname(__file__), "assets", "img", f"{filename}.png"
    )
    with open(img_filepath, "wb") as f:
        f.write(img_data)

    # Return a response with status code 200
    return make_response("Image uploaded successfully.", 200)
