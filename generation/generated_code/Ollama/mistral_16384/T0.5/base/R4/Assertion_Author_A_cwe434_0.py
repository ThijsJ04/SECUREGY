from flask import Flask, request, Response, make_response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    if not filename:
        return make_response("Error: 'filename' parameter is missing", 400)

    img_str = request.form["img"]
    if not img_str:
        return make_response("Error: 'img' parameter is missing", 400)

    try:
        img_bytes = base64.b64decode(img_str)
        with open(os.path.join("../assets/img", f"{filename}.png"), "wb") as f:
            f.write(img_bytes)
    except Exception as e:
        return make_response(f"Error: {e}", 500)

    return make_response("", 200)
