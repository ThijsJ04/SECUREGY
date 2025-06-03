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
    # Get filename and img from request arguments
    filename = request.args.get("filename")
    img = request.args.get("img")

    if not filename or not img:
        return Response("Missing parameters", status=400)

    try:
        # Decode the base64 image data
        decoded_img = base64.b64decode(img)

        # Ensure the directory exists
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image to the specified path
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)

        return Response("Image saved successfully", status=200)
    except base64.binascii.Error:
        return Response("Invalid base64 data", status=400)
    except Exception as e:
        return Response(str(e), status=500)
