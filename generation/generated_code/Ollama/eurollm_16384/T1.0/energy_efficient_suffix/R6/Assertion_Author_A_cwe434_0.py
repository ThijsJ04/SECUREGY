from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Handles image uploads.
    """
    filename = request.form["filename"]  # Get the filename from the request form data
    content_type, img_data = request.stream.read()  # Read the image data stream

    img_data = base64.b64decode(img_data)  # Decode the base64 encoded image

    with open(
        "../assets/img/" + filename + ".png", "w+b"
    ) as f:  # Save the image to a file in assets folder
        f.write(img_data)

    data = {"status": "success", "filename": filename}
    return Response(response=str(data), status=200, mimetype="application/json")
