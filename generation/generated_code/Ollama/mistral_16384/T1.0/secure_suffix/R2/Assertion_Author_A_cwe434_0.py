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
    try:
        filename = request.args.get("filename")
        img_data = request.form["img"]
        img_bytes = base64.b64decode(img_data)
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(img_bytes)
        return Response(status=200)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
