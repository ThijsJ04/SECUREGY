from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")
    decoded_img = base64.b64decode(img_data)
    file_path = f"../assets/img/{filename}.png"
    with open(file_path, "wb") as f:
        f.write(decoded_img)
    return Response(status=200)
