from flask import Flask, request, Response, make_response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img_data = request.values.get("img", None)

    if not all([filename, img_data]):
        return make_response("Missing required parameters.", 400)

    try:
        decoded_img = base64.b64decode(img_data)
    except (TypeError, ValueError):
        return make_response("Invalid base64 encoded image data.", 400)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_img)

    return make_response("Image uploaded successfully.", 200)
