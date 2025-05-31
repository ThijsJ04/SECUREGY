from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    # Get the "filename" from the request using request.form["filename"]
    filename = request.form.get("filename")

    # Get the "img" parameter from the request using request.data
    img_data = request.data

    # Decode the base64 encoded data to an image
    encoded_img = base64.b64decode(img_data)

    # Open a binary writer (we're writing bytes, not strings!)
    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(encoded_img)

    return Response('Image uploaded successfully', status=200)