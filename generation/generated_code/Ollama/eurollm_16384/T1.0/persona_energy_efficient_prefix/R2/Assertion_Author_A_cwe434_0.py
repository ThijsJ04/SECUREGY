from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]  # Get the filename from the request.
    img = request.files["img"]  # Get the image file as a File instance.

    decoded_image = base64.b64decode(img.read())  # Decode the image data using base64.

    with open(
        f"../assets/img/{filename}.png", "wb"
    ) as file:  # Save the image to a file.
        file.write(decoded_image)

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
