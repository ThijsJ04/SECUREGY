from flask import Flask, request, Response, make_response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    if not filename:
        return make_response("Missing 'filename' parameter.", 400)

    img_data = request.values.get('img', None)
    if not img_data:
        return make_response("Missing 'img' parameter.", 400)

    try:
        decoded_img = base64.b64decode(img_data)
    except (TypeError, ValueError):
        return make_response("Invalid base64 encoded image.", 400)

    filepath = os.path.join("../assets/img", filename + ".png")
    with open(filepath, "wb") as f:
        f.write(decoded_img)

    return make_response("Image uploaded successfully.", 200)