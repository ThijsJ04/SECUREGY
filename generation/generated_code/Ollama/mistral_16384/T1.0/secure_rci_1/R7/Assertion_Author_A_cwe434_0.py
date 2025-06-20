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
    if "img" not in request.json or "filename" not in request.args:
        return jsonify(
            {"error": 'Missing "img" parameter or "filename" query param'}
        ), 400

    img_data = request.json["img"]
    filename = request.args.get("filename")

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    return Response(status=200)
