from flask import Flask, request, Response, make_response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_str = request.form["img"]
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(base64.b64decode(img_str))
    return make_response(Response(), 200)
