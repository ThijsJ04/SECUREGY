from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Assuming 'filename' is a query parameter
    file_data = request.files[
        "img"
    ]  # Assuming 'img' is the file parameter in the request body

    if not filename or not file_data:
        return Response(status=400)

    decoded_image = base64.decodestring(file_data).decode(
        "utf-8"
    )  # Decoding the image data from base64

    with open(f"../assets/img/{filename}.png", "wb") as img_file:
        img_file.write(decoded_image)  # Saving the image to file

    return Response(status=200, mimetype="application/octet-stream")
