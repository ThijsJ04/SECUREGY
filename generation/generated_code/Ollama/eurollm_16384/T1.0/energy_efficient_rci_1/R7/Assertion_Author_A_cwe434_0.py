from flask import Flask, request, Response, send_file
import base64
from PIL import Image
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png" using send_file().
    :return: a Response with status code equals to 200.
    """
