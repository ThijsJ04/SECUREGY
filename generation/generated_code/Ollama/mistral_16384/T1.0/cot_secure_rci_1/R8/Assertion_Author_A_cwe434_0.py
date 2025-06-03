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
    if not request.method == "POST":
        return Response(status=405)

    filename = request.form.get("filename")
    if not filename:
        return Response(status=400)

    img_data = request.form["img"]
    if not img_data:
        return Response(status=400)

    decoded_img = base64.b64decode(img_data)

    filepath = os.path.join(current_app.root_path, "assets", "img", filename + ".png")
    with open(filepath, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
