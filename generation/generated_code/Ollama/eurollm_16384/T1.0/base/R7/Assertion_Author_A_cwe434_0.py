from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """Handles image file uploads."""
    if "filename" not in request.args:
        return Response(status=400)  # Missing filename parameter

    if "img" not in request.files or request.files["img"].fileno() == 0:
        return Response(status=406)  # No image file sent

    with open("../assets/img/{filename}.png".format(**request.args), "wb") as out_file:
        data = base64.decodebytes(request.files["img"].read())
        out_file.write(data)
    return Response("Image saved successfully", status=200, mimetype="text/plain")
