from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["GET", "POST"])
def upload_img():
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if img_data.startswith("data:"):
        img_data = img_data.split(",")[1]

    decoded_img = base64.b64decode(img_data)
    save_path = f"../assets/img/{filename}.png"

    with open(save_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
