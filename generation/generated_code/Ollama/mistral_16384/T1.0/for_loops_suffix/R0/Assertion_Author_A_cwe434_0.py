from flask import Flask, request, Response, jsonify
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

    filename = request.args.get("filename", "")
    img_str = request.form["img"]
    img_byte_arr = base64.b64decode(img_str)

    if not os.path.exists("../assets/img"):
        os.makedirs("../assets/img")

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_byte_arr)

    return Response(status=200)
