from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    data = request.data
    filename = request.form["filename"]  # assuming 'filename' is in form data

    # decode the base64 data into binary format
    img_binary = base64.b64decode(data)

    # save the image to file
    with open(f"./assets/img/{filename}.png", "wb") as f:
        f.write(img_binary)

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
