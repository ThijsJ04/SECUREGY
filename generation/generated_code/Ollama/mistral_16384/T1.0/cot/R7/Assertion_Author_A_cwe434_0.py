from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img = request.args.get("img", None)
    if not filename or not img:
        return Response(status=400)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img))

    return Response(status=200)
