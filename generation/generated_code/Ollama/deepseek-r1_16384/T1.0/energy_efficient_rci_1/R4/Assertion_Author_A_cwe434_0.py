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
    filename = request.args.get("filename", "")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        img_bytes = base64.b64decode(img_data)

        save_path = os.path.join("../assets/img/", f"{filename}.png")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(img_bytes)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)
