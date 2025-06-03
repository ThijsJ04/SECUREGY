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
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Decode base64 string
    try:
        decoded_img = base64.b64decode(img_data)
    except:
        return Response(status=500)  # Return 500 if decoding fails

    # Create directory if it doesn't exist
    os.makedirs("../assets/img", exist_ok=True)

    # Save image to file
    img_path = f"../assets/img/{filename}.png"
    with open(img_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
