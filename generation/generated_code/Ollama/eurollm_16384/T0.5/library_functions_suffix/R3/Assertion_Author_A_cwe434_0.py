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
    filename = request.form.get("filename")

    # Check if the file was uploaded, then decode it and save it as png image
    if "img" in request.files:
        file = request.files["img"]
        if file:
            base64_data = base64.b64decode(file.read())  # Decodes the image data
            pil_image = Image.open(
                BytesIO(base64_data)
            )  # Converts the decoded data to a PIL image
            pil_image.save(
                "../assets/img/{filename}.png".format(filename=filename), "PNG"
            )
            return Response(status=200)
    else:
        return Response(status=403)  # Return 403 if no image file was uploaded
