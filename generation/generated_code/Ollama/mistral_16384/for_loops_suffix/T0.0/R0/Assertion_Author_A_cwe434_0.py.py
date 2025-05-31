from flask import Flask, request,Response, make_response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_data = request.args.get('img', None)

    if not filename or not img_data:
        return make_response("Missing required parameters", 400)

    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return make_response("Error decoding image data", 500)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_img)

    return make_response("Image uploaded successfully", 200)