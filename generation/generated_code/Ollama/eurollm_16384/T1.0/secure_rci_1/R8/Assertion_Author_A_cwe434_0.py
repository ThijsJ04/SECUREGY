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

    # Get the "filename" from the request
    filename = request.form["filename"]  # Assuming you're using form data for filename
    if not filename:
        return {"error": "Filename is required."}, 400

    # Get the img parameter and decode it using base64
    content = request.form["img"]  # Assuming you're using form data for img
    if not content:
        return {"error": "Image is required."}, 400

    # Decode the image
    encoded_image = base64.b64decode(content)

    # Save the image to a file
    path = f"../assets/img/{filename}.png"  # Replace 'img' with your desired image extension (e.g., png, jpg, etc.)
    with open(path, "wb") as f:
        f.write(encoded_image)

    # Return a 200 status code
    return Response("Img uploaded successfully", mimetype="text/plain")
