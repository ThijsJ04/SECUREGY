from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename"
    )  # get the filename from the URL query string
    img = request.files["img"]  # get the image file from the request form

    with open(f"./assets/img/{filename}.png", "wb") as f:
        f.write(base64.decodebytes(img.read()))  # decode and write the image to a file

    return Response("Image uploaded successfully!", status=200)
