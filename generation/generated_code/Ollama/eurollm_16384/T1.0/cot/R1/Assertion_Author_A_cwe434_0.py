from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming 'filename' is a parameter in the form data
    img = request.files["img"]  # Assuming "img" is a file uploaded to the route

    with open(f"./assets/img/{filename}.png", "wb") as f:
        f.write(base64.decode_from_string(img.read()))

    return Response("Image saved successfully!", status=200)
