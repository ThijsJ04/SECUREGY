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
    # Extract filename and img data from request form
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    # Ensure the directory exists
    dir_path = "../assets/img"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Decode base64 string to bytes
    try:
        image_bytes = base64.b64decode(img_data)
    except Exception as e:
        return Response(f"Error decoding base64: {str(e)}", status=500)

    # Save the image file
    filepath = os.path.join(dir_path, f"{filename}.png")
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    return Response("Image uploaded successfully.", status=200)
