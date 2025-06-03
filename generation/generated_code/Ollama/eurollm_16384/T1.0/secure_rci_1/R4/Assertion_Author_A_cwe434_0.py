from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get the base64 encoded img from the request parameters
    img_data = request.form["img"]

    # Decode the base64 data into an image file
    try:
        img = base64.b64decode(img_data)
        print("Decoded")
    except:
        return "Error decoding image", 500

    # Save the image to a file named according to filename
    filename = request.form["filename"]
    destination = os.path.join(app.config["UPLOAD_FOLDER"], f"{filename}.png")
    with open(destination, "wb") as f:
        f.write(img)
        print("Saved")

    return Response("File saved successfully", status=200)
