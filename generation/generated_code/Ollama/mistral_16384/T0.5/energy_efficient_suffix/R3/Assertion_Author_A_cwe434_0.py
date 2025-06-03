from flask import Flask, request, Response, current_app
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
    img_data = base64.b64decode(request.form["img"])

    if not filename or not img_data:
        return Response("Missing data", status=400)

    filepath = os.path.join(current_app.root_path, "assets/img", f"{filename}.png")
    with open(filepath, "wb") as f:
        f.write(img_data)

    return Response("Image saved successfully", status=200)
