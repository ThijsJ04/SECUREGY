from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the filename from the request
    filename = request.args.get("filename")

    if not filename:
        return "Error: No filename provided", 400

    # Get the img parameter from the request
    data = request.files["img"]
    if not data:
        return "Error: No image file uploaded", 406

    # Decode the base64 string to an image
    with open(f"../assets/img/{filename}.png", "wb") as f:
        encoded_data = data.read()
        decoded_data = base64.decodebytes(encoded_data)
        f.write(decoded_data)

    return "Image uploaded successfully", 200
