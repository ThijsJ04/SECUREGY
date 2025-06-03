from flask import Flask, request, Response, jsonify
import base64
from PIL import Image

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "data" parameter (JSON formatted with "content-type: application/json")
    containing information about the image from the request.
    Use base64 to decode the "data" parameter and create an Image object.
    Save the image to the file "../assets/img/{filename}.png".
    :return: a Response with status code equals to 200.
    """
