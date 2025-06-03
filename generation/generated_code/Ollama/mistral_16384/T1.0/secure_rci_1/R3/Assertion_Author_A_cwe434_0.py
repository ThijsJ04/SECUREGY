from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    if not filename:
        return Response(status=400)

    img_str = request.values.get("img", None)
    if not img_str:
        return Response(status=400)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        decoded_img = base64.b64decode(img_str)
        f.write(decoded_img)

    return Response(status=200)
