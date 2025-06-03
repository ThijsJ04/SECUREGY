from flask import Flask, request, Response, current_app
import base64
import io

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    if "filename" not in request.args or "img" not in request.args:
        return Response("Missing parameters.", status=400)

    filename = request.args["filename"]
    img_b64 = request.args["img"]

    img_bytes = base64.b64decode(img_b64)

    with io.BytesIO(img_bytes) as buffer:
        buffer.name = f"../assets/img/{filename}.png"
        with open(buffer, "wb") as out_file:
            out_file.write(img_bytes)

    return Response("Image uploaded successfully.", status=200)
