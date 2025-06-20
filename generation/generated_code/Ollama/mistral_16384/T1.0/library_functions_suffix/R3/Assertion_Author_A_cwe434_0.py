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
    filename = request.args.get("filename")
    img_bytes = base64.b64decode(request.form["img"])

    # Ensure the directory exists before saving the file
    if not os.path.exists("../assets/img"):
        os.makedirs("../assets/img", exist_ok=True)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_bytes)

    return Response(response="OK", status=200, mimetype="application/json")
