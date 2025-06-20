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
    # Get the filename from the request
    filename = request.form["filename"]

    # Get the img parameter from the request and decode it using base64
    img_data = base64.b64decode(request.files["img"].read())

    # Save the image to the file "../assets/img/{filename}.png"
    destination = open(f"./assets/img/{filename}.png", "wb")
    destination.write(img_data)
    destination.close()

    return Response(
        "Image uploaded successfully", status=200, mimetype="application/json"
    )
