from flask import Flask, request, Response, current_app
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
    img_data = request.form["img"]

    # Decode base64 data
    decoded_img = base64.b64decode(img_data)

    # Save the decoded image to the specified file path
    asset_folder = os.path.join(current_app.root_path, "static", "assets", "img")
    file_path = os.path.join(asset_folder, f"{filename}.png")
    with open(file_path, "wb") as out:
        out.write(decoded_img)

    # Create a Response object with status code 200
    return Response(status=200)
