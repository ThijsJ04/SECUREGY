from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    data = request.data
    base64_string = base64.b64decode(data)
    img = Image.open(BytesIO(base64_string))
    filename = "".join(request.form.getlist("filename"))
    path = os.path.join("..", "assets", "img", filename + "." + img.format)
    img.save(path)
    return Response("Image saved successfully", status=200, mimetype="text/plain")
