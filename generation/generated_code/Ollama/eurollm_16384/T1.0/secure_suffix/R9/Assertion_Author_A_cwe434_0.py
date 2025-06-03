from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """Handles image uploads."""

    filename = request.args.get(
        "filename", default="default"
    )  # get the "filename" from the request
    img = request.files["img"]  # retrieve the uploaded image file
    data_b64 = img.read()  # read the binary data of the uploaded image file

    encoded_image = base64.b64encode(data_b64)  # encode the image as Base64 string
    response = Response(
        content=encoded_image, status=200, mimetype="image/png"
    )  # return a response with the encoded image and a 200 status code

    filename += (
        ".png"  # add .png extension to the filename if it doesn't already have one
    )
    directory = os.path.join(
        os.getcwd(), "assets/img"
    )  # create an absolute path for the assets folder
    if not os.path.exists(
        directory
    ):  # check if the assets folder exists; if not, create it
        os.makedirs(directory)

    with open(
        os.path.join(directory, filename), "wb"
    ) as file:  # save the encoded image to a file in the assets folder
        file.write(data_b64)

    return response  # return the encoded image with 200 status code


app.run()
