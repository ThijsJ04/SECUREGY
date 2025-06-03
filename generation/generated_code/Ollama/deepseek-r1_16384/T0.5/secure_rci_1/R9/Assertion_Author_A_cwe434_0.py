from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.values.get("filename")
    img_data = request.values.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except Exception as e:
        print(f"Error decoding image: {e}")
        return Response(status=500)

    path = os.path.join("../assets/img", filename + ".png")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, "wb") as f:
            f.write(img_bytes)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)

    return Response(status=200)
