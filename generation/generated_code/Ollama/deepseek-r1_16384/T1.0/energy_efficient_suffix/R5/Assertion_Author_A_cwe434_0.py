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
    filename = request.form.get("filename")
    img_str = request.form.get("img")

    try:
        # Decode the base64 string into bytes
        img_bytes = base64.b64decode(img_str)
    except:
        return Response(status=500)  # Return 500 if decoding fails

    # Ensure the directory exists
    import os

    directory = "../assets/img/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the image file
    file_path = os.path.join(directory, f"{filename}.png")
    with open(file_path, "wb") as img_file:
        img_file.write(img_bytes)

    return Response(status=200)
