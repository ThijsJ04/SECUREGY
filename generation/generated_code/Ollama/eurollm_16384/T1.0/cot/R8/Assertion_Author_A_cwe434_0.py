from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Get the filename from the query parameter
    if not filename:
        return "Error: Filename is required", 400

    file = request.files["img"]  # Get the image file uploaded by the user
    if not file or "img" not in request.files:
        return "Error: No image provided", 400

    decoded_data = base64.b64decode(file.read())  # Decode the base64 encoded data
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(decoded_data)  # Write the decoded data to a file

    return Response("Image saved successfully", status=200, mimetype="image/png")
