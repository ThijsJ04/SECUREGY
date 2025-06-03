from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]  # get the filename from the form data
    img = request.files["img"]  # get the image file from the request

    decoded_img = base64.b64decode(img.read())  # decode the image using base64
    with open(f"../assets/img/{filename}.png", "wb") as f:  # save the image to a file
        f.write(decoded_img)

    return Response("Image uploaded successfully", status=200, mimetype="text/plain")
