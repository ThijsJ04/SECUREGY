from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_str = request.form["img"]
    with open(f"../assets/img/{filename}.png", "wb") as f:
        img = base64.b64decode(img_str)
        f.write(img)
    return Response("Image saved successfully", status=200, mimetype="text/plain")
