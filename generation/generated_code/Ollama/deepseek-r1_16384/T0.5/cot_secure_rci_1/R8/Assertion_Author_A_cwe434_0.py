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
        decoded_data = base64.b64decode(img_data)
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return Response(status=500)

    path = f"../assets/img/{filename}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb") as f:
        f.write(decoded_data)

    return Response(status=200)
