from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming the filename is passed in a form field
    data = request.files["img"]  # Assuming the image is passed as an input file

    # Decode the base64 encoded data
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(
            base64.decodebytes(data.read())
        )  # Read the data from the input file and decode it using base64

    return Response("Image uploaded successfully", status=200)
