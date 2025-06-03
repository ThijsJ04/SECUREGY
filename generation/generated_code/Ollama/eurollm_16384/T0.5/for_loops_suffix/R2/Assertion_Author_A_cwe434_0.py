from werkzeug.datastructures import FileStorage
from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request
    filename = request.args.get("filename")
    img = request.files["img"]  # Assuming 'img' is a file field in your form

    if not filename:
        return Response(status=400)

    # Use base64 to decode the "img" parameter
    data_url = img.read()
    data_b64 = base64.b64encode(data_url).decode("utf-8")

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(data_url)

    return Response(
        status=200,
        headers={"Content-Type": "image/png"},
        mimetype="application/octet-stream",
    )
