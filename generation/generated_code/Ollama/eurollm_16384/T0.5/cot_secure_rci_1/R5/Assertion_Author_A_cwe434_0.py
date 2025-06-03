from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img = request.files["img"]
    data = base64.b64decode(
        img.read()
    )  # Read the image data from the file-like object `img`
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(data)
    return Response(status=200)
