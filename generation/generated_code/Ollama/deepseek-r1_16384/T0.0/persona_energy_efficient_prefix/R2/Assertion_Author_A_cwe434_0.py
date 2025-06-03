from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename") or request.form.get("filename")
    img_str = request.args.get("img") or request.form.get("img")

    if not filename or not img_str:
        return Response(status=400)

    try:
        img_bytes = base64.b64decode(img_str)
    except Exception as e:
        return Response(status=400, response=str(e))

    filepath = f"../assets/img/{filename}.png"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(img_bytes)

    return Response()
