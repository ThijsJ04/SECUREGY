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

    # Get the filename and img from the request
    filename = request.args.get("filename")
    img_data = request.files[
        "img"
    ]  # Assuming 'img' is a file uploaded in the request form

    # Decode the base64-encoded image data
    try:
        img_data = img_data.read()
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return {"error": f"Failed to decode the image: {str(e)}"}, 500

    # Save the image to a file
    try:
        path = os.path.join("..", "assets", "img", filename + ".png")
        with open(path, "wb") as f:
            f.write(decoded_img)
        return {"message": "Image saved successfully."}, 200
    except Exception as e:
        return {"error": f"Failed to save the image: {str(e)}"}, 500
