from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")
    img_data = request.form.get("img")
    image_bytes = base64.b64decode(img_data)
    save_path = f"../assets/img/{filename}.png"
    with open(save_path, "wb") as f:
        f.write(image_bytes)
    return Response(status=200)
