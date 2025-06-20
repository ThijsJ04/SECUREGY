from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    # Decode the base64 string
    decoded_img = base64.b64decode(img_data)

    # Create directory if it doesn't exist
    os.makedirs("../assets/img", exist_ok=True)

    # Save the image to file
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
