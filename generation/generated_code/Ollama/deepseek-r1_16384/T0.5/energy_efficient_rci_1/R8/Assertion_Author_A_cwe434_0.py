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
    # Get filename and img parameters from request
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Check if both parameters are provided
    if not filename or not img_data:
        return Response("Missing required parameters", status=400)

    try:
        # Decode the base64 encoded image data
        decoded_data = base64.b64decode(img_data)

        # Ensure the directory exists
        directory = os.path.dirname("../assets/img/")
        os.makedirs(directory, exist_ok=True)

        # Save the file
        file_path = os.path.join("../assets/img/", f"{filename}.png")
        with open(file_path, "wb") as f:
            f.write(decoded_data)

        return Response(status=200)
    except Exception as e:
        return Response(str(e), status=500)
