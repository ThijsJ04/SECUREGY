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
    img_data = request.form["img"]
    filename = request.args.get("filename")

    # Decode base64 image data and save it to the specified file path
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
