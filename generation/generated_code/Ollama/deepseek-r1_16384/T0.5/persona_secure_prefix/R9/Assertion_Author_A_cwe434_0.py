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
    filename = request.args.get("filename", "", str)
    img_data = request.args.get("img", "", str)

    # Decode base64 data
    decoded_img = base64.b64decode(img_data)

    # Construct file path
    filepath = os.path.join("../assets/img", f"{filename}.png")

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Save the image
    with open(filepath, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
