from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename", default="default.png"
    )  # optional parameter for filename
    with request.fopen("rb") as image_file:  # read binary data from the request body
        img_data = base64.b64decode(image_file.read())
    path = "../assets/img/" + filename + ".png"
    with open(path, "wb") as f:  # write binary data to a file
        f.write(img_data)
    return Response(status=200)
