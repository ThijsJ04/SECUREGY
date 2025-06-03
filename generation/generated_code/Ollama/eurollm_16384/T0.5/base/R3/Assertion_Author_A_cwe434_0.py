from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Get the filename from the form data
    data = request.files["img"]  # Get the image file as a stream
    img_data = base64.b64decode(data)  # Decode the image data using base64

    with open(f"../assets/img/{filename}.png", "wb") as f:  # Save the image to a file
        f.write(img_data)

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
