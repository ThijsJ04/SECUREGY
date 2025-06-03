from flask import Flask, request, Response
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming 'filename' is a form field in the POST request
    data = request.files[
        "img"
    ]  # Assuming 'img' is a file uploaded via the POST request

    if not data:
        return Response(status=400, mimetype="application/json")

    # Decode the image from base64 and save it to disk
    decoded_data = base64.b64decode(data)
    img_bytes = BytesIO(decoded_data)
    img = Image.open(img_bytes)

    # Save the image to the file "../assets/img/{filename}.png"
    save_path = f"../assets/img/{filename}.png"
    with open(save_path, "wb") as f:
        img.save(f)

    return Response(status=200, mimetype="image/png")
