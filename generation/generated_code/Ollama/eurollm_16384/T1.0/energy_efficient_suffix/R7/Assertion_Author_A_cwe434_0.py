from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "default")
    data = request.data

    # Decode the image using base64
    b64_encoded_data = str(base64.b64decode(data))

    with open(f"../assets/img/{filename}.png", "wb") as file:
        file.write(b64_encoded_data)

    return Response("File saved successfully", status=200, mimetype="application/json")
