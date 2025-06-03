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
    # Get filename and img from query parameters
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Decode the base64 encoded image data
    decoded_img = base64.b64decode(img_data)

    # Ensure the directory exists
    os.makedirs("../assets/img", exist_ok=True)

    # Save the image to the specified path
    file_path = os.path.join("../assets/img", f"{filename}.png")
    with open(file_path, "wb") as f:
        f.write(decoded_img)

    # Return a response with status code 200
    return Response(status=200)
