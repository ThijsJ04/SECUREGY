from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # get filename from query string
    data = request.files[
        "img"
    ]  # get image file from form data (assuming it's a form on the client-side)
    encoded_data = base64.b64decode(data)  # decode base64 encoded data
    with open("../assets/img/{}.png".format(filename), "wb") as f:  # save image to file
        f.write(encoded_data)
    return Response(status=200)  # return 200 status code and empty response body
