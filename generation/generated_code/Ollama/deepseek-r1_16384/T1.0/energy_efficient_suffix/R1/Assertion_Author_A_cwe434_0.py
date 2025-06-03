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
    if request.method != "POST":
        return Response("Method Not Allowed", status=405)

    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        decoded_data = base64.b64decode(img_data)
        filepath = f"../assets/img/{filename}.png"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "wb") as file:
            file.write(decoded_data)

        return Response(status=200)
    except Exception as e:
        app.logger.error(f"Error during image upload: {e}")
        return Response("Internal server error", status=500)
