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
    img_data = request.values.get("img")
    if not (filename and img_data):
        return Response(status=400)

    # Save decoded image to "../assets/img/{filename}.png"
    filepath = os.path.join(
        current_app.root_path, "..", "static", "assets", "img", f"{filename}.png"
    )
    with open(filepath, "wb") as f:
        decoded_img = base64.b64decode(img_data)
        f.write(decoded_img)

    # Return a Response with status code equals to 200
    return Response(status=200)
