from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")  # Get the "filename" from the form data
    img = base64.b64decode(
        request.files["img"].read()
    )  # Decode the image data with base64

    # Save the image to the file
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(img)

    return Response("Image saved successfully!", status=200, mimetype="text/plain")
