from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Assuming filename is in the URL
    data = request.data

    # Decode base64 data to image
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.decodebytes(data))

    return Response("Image saved successfully", status=200)
