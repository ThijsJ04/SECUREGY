from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]
    img_data = request.files["img"]
    decoded_img_data = base64.b64decode(img_data)
    with open("../assets/img/" + filename, "wb") as f:
        f.write(decoded_img_data)
    return Response(status=200)
