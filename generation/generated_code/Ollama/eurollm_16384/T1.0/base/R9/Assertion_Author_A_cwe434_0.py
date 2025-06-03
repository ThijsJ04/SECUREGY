from flask import Flask, request, Response
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    data = request.get_json()
    filename = (
        data.get("filename") or "default"
    )  # Provide a default filename if not provided
    if not filename:
        return {"error": "Please provide a filename."}, 400

    # Decode the "img" parameter using base64 and get its raw data.
    decoded_data = base64.b64decode(request.files["image"].read())
    raw_data = decoded_data

    # Save the image to the file "../assets/img/{filename}.png" using PIL.
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(raw_data)

    return {"message": "Image uploaded successfully."}, 200
