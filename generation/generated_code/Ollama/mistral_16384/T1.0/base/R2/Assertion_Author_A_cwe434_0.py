from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img_data = request.params["img"]
    img_bytes = base64.b64decode(img_data)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
