from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming the filename is stored in a form field called 'filename'
    data = request.files["img"]  # Assuming the image is stored as a file named 'img'

    with open(
        f"../assets/img/{filename}.png", "wb"
    ) as f:  # Create a new file in assets folder with the given filename
        f.write(
            base64.b64decode(data)
        )  # Decode the image data from base64 and write it to the file

    return Response("Image uploaded successfully", status=200)
