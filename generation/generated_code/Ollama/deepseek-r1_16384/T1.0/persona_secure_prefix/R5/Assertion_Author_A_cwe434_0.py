from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_data = base64.b64decode(img_data)
    except Exception as e:
        return Response(status=500)

    directory = os.path.join("../assets/img")
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{filename}.png")

    try:
        with open(file_path, "wb") as f:
            f.write(decoded_data)
    except Exception as e:
        return Response(status=500)

    return Response(status=200)
