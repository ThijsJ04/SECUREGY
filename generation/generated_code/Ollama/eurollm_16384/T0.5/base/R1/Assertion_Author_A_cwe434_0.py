from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Get the "filename" from the request
    data = request.files["img"]  # Get the "img" parameter from the request

    # Convert the image to bytes using base64 encoding
    img_bytes = data.read()

    # Save the image to a file in the assets folder
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_bytes)

    return Response(
        "Image uploaded successfully!", status=200, mimetype="application/json"
    )
