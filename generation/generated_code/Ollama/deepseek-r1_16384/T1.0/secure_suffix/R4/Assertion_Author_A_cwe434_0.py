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

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Remove data URL prefix if present
    if img_data.startswith("data:image/png;base64,"):
        img_data = img_data.split(",", 1)[1]

    try:
        decoded_img = base64.b64decode(img_data)

        # Ensure directory exists
        os.makedirs("../assets/img", exist_ok=True)

        file_path = f"../assets/img/{filename}.png"
        with open(file_path, "wb") as f:
            f.write(decoded_img)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response("Failed to save image", status=500)
