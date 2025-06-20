from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    filename = request.args.get("filename")
    img_base64 = request.form["img"]
    img_byte_array = base64.b64decode(img_base64)

    with open(f"../assets/img/{filename}.png", "wb") as file:
        file.write(img_byte_array)

    return Response(status=200)
