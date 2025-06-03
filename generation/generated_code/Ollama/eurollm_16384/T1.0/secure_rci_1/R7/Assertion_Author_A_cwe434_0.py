from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # assuming form is used for uploading the image
    img = request.files[
        "img"
    ]  # img is a file-like object, use decode to convert it into bytes
    img_bytes = base64.b64decode(
        img
    )  # decodes base64 encoded data and returns an array of bytes
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_bytes)  # writes the decoded data to a file
    return Response("Image saved successfully", status=200, mimetype="image/png")
