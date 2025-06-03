from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    content_type, img_data = request.stream.read()
    # decode the base64 string into a byte stream using PIL (Pillow) library
    from PIL import Image

    img = Image.open(io.BytesIO(base64.b64decode(img_data)))
    path = f"../assets/img/{filename}.png"
    if not img.is_modified():  # check if the image is a JPEG or PNG, otherwise ignore
        with open(path, "wb") as out:
            out.write(img.tobytes())

    return Response(status=200)
