from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = (
        request.form.get("filename") or request.args.get("filename") or "default.png"
    )
    img_data = request.form.get("img") or request.args.get("img")

    if img_data.startswith("data:image/png;base64,"):
        img_data = img_data.split(",")[1]

    try:
        image_bytes = base64.b64decode(img_data)
    except:
        return Response(status=500)

    save_dir = "../assets/img"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, f"{filename}.png")

    try:
        with open(filepath, "wb") as f:
            f.write(image_bytes)
    except:
        return Response(status=500)

    return Response(status=200)
