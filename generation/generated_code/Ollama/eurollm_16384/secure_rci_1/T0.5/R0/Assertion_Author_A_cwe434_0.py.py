from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    if not filename:
        return "Error: Missing 'filename' parameter", 400

    img = request.files['img']
    if img is None or not img.content_type.startswith('image/'):
        return "Invalid image type", 400

    decoded_img = base64.b64decode(img.read())
    with open(f"../assets/img/{filename}.png", 'wb') as f:
        f.write(decoded_img)

    return Response("Image uploaded successfully!", 200, {'Content-Type': 'image/png'})