from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")
    data = request.files[
        "img"
    ]  # Assuming the image is being sent in a form with key 'img'

    # Use base64 to decode the image data
    img_data = base64.b64decode(data)

    with open(f"./assets/img/{filename}.png", "wb") as file:
        file.write(img_data)

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
