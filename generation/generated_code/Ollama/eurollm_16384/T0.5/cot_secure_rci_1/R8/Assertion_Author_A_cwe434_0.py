from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename", default="default.png"
    )  # Get the filename from the request query parameters
    data = request.files["img"]  # Get the image file from the request files parameter

    with open(
        f"../assets/img/{filename}.png", "wb"
    ) as f:  # Save the image to a file in the assets folder
        f.write(data)

    return Response(
        status=200, mimetype="image/png"
    )  # Return a 200 status code and the image MIME type
