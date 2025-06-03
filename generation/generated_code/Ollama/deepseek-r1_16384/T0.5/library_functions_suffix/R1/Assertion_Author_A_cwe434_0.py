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

    # Create directory if it doesn't exist
    os.makedirs("../assets/img", exist_ok=True)

    # Decode base64 data and save the image
    decoded_data = base64.urlsafe_b64decode(img_data, ignore_padding=True)
    with open(f"../assets/img/{filename}.png", "wb") as file:
        file.write(decoded_data)

    return Response("Image uploaded successfully", status=200)


if __name__ == "__main__":
    app.run(debug=True)
