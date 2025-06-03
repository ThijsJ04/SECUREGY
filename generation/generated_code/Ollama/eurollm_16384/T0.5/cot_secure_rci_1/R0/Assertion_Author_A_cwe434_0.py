from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # get the filename from GET parameters
    img_data = request.form.get("img").encode(
        "utf-8"
    )  # get the image data from form data (assuming it's encoded in utf-8)
    decoded_img_data = base64.b64decode(img_data)
    with open(f"./assets/img/{filename}.png", "wb") as f:  # save the image to a file
        f.write(decoded_img_data)
    return Response(content=decoded_img_data, mimetype="image/png")
