from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Get the "filename" from the request
    img = request.files["img"]  # Get the "img" parameter from the request
    data = img.read()
    base64_data = base64.b64encode(data).decode("utf-8")

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(
            base64.decodebytes(base64_data)
        )  # Decode the base64 data and write it to a file

    return Response("Image uploaded successfully!", status=200)
