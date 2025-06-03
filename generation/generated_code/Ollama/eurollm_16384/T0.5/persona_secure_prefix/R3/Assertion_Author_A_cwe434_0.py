from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename", default="image.png"
    )  # get filename from the request query string
    data = request.files["img"]  # get the image file from the request

    encoded_data = base64.b64decode(data)  # decode the image data using base64
    open("../assets/img/{}.png".format(filename), "wb").write(
        encoded_data
    )  # save the image to a file

    return Response(
        status=200, mimetype="image/png"
    )  # return a response with status code 200 and content type 'image/png'
