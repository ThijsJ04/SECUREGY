from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request
    filename = request.form[
        "filename"
    ]  # Assuming the filename is sent in the form data

    # Get the "img" parameter from the request
    img_data = request.files[
        "image"
    ]  # Assuming the image file is sent as a multipart/form-data

    # Decode the img_data using base64
    decoded_data = base64.b64decode(img_data)

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_data)

    return Response("Image saved successfully!", status=200, mimetype="text/plain")
