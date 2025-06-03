from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        decoded_image = base64.b64decode(img_data)
        directory = os.path.dirname("../assets/img/")
        os.makedirs(directory, exist_ok=True)
        save_path = os.path.join("../assets/img/", filename + ".png")
        with open(save_path, "wb") as f:
            f.write(decoded_image)
    except Exception as e:
        return Response(str(e), status=500)

    return Response("Image saved successfully", status=200)
