from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Get the "filename" from the request
    data = request.files["img"]  # Get the "img" parameter from the request

    # Decode the image using base64
    encoded_data = data.read()
    decoded_data = base64.b64decode(encoded_data)

    # Save the image to the file
    with open("../assets/img/" + filename + ".png", "wb") as f:
        f.write(decoded_data)

    return Response(
        status=200, mimetype="image/png"
    )  # Return a response with status code 200 and image type png
