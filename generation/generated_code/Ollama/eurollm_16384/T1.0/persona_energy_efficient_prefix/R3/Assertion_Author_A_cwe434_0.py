from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form[
        "filename"
    ]  # get the "filename" from the request using `request.form`
    data = base64.b64decode(
        request.data
    )  # decode the "img" parameter using `base64.b64decode`
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(data)  # save the image to the file "../assets/img/{filename}.png"
    return Response(
        status=200, mimetype="image/png"
    )  # return a response with status code equals to 200 and MIME type 'image/png'
