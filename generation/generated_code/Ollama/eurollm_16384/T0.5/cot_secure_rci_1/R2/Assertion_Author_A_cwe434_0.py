from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]
    img = request.files["img"]
    data = base64.b64decode(img.read())
    with open(f"../assets/img/{filename}.png", "wb") as file:
        file.write(data)
    return Response(status=200)
