from flask import Flask, request,Response, make_response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = request.form['img']

    with open(f"../assets/img/{filename}.png", "wb") as f:
        decoded_image = base64.b64decode(img_data)
        f.write(decoded_image)

    return make_response("Image saved successfully.", 200)