from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get the filename from the request
    try:
        filename = request.args[
            "filename"
        ]  # Assuming 'filename' is available as an argument in URL
    except KeyError:
        abort(400)

    # Get the image data from the request and decode it with base64
    img_data = request.files.get("img")
    if img_data is None:
        return "No image file uploaded", 415  # No file part in request
    try:
        decoded_img = base64.b64decode(img_data)  # Decoding base64 data to bytes
    except Exception as e:
        return str(e), 400

    # Save the image to a file
    with open("../assets/img/" + filename, "wb") as f:
        f.write(decoded_img)  # Write bytes directly (without converting back to string)

    return Response(status=200)
