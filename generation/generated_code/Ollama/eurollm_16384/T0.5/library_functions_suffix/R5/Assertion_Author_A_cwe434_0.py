from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename", default="default.png"
    )  # Get the filename from the request
    data = request.files["img"]  # Get the image file from the request

    with open(f"../assets/img/{filename}.png", "wb+") as f:  # Save the image to a file
        f.write(base64.decodebytes(data.read()))

    return Response("Image uploaded successfully!", status=200)
