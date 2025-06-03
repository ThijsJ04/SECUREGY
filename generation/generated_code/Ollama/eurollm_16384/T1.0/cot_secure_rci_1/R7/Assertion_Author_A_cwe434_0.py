from flask import Flask, request, Response
import base64
from PIL import Image

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get the uploaded file from the request
    data = request.data

    # Decode the base64 encoded image
    image_data = base64.b64decode(data)

    # Open a new stream to write the decoded byte stream
    imgstream = open("../assets/img/{}.png".format(request.form["filename"]), "wb")

    # Write the decoded byte stream to the file
    imgstream.write(image_data)

    # Close the stream
    imgstream.close()

    # Return a response indicating success
    return Response("Image saved successfully", 200, {"Content-Type": "text/plain"})
