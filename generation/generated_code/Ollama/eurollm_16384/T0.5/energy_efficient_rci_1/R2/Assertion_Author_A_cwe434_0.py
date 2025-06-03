from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """Uploads an image and saves it as a png file."""
    filename = request.form["filename"]  # Assuming the filename is in the form data
    img = request.files["img"]  # Assuming the img parameter is in the request
    image_data = base64.b64decode(str(img))

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(image_data)

    return Response("Image saved successfully", status=200)
