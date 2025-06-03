from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        image_bytes = base64.b64decode(img_data)
        dir_path = "../assets/img"
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, f"{filename}.png")
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)
