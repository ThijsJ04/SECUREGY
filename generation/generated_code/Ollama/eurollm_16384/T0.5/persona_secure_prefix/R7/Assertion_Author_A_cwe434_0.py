from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Get the "filename" from the request
    img = request.files["img"]  # Get the "img" parameter from the request

    if not os.path.exists("../assets/img"):
        os.makedirs("../assets/img")  # Create the assets directory if it doesn't exist

    decoded_img = base64.b64decode(img.read())  # Decode the image using base64
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_img)  # Write the decoded image to a file

    return Response(
        "Image uploaded successfully!", status=200, mimetype="application/json"
    )
