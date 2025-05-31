from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get("filename")
    img = request.files["img"]
    img_data = base64.b64decode(img.read())  # Read the image data from the file-like object img
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)  # Write the decoded image data to a file
    return Response('', status=200, mimetype='image/png')