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
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except (base64.binascii.Error, TypeError) as e:
        print(f"Invalid base64 data: {e}")
        return Response(status=400)

    save_dir = os.path.join("../assets", "img")
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{filename}.png")

    try:
        with open(file_path, "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        print(f"Error saving file: {e}")
        return Response(status=500)

    return Response(status=200)
