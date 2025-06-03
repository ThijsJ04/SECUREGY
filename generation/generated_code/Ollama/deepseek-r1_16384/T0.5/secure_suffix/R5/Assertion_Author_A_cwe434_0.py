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
    try:
        # Extract filename and img data from request
        filename = request.form.get("filename", "").strip()
        img_data = request.form.get("img", "")

        if not filename or not img_data:
            return Response("Missing parameters", status=400)

        # Validate filename to prevent path traversal
        if os.path.basename(filename) != filename:
            return Response("Invalid filename", status=400)

        # Decode base64 image data
        try:
            decoded_img = base64.b64decode(img_data)
        except binascii.Error:
            return Response("Invalid base64 data", status=400)

        # Save the image file
        save_path = os.path.join("../assets/img/", filename + ".png")
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(decoded_img)

        return Response("Image saved successfully", status=200)

    except Exception as e:
        # Return generic error message for security reasons
        return Response("Internal server error", status=500)
