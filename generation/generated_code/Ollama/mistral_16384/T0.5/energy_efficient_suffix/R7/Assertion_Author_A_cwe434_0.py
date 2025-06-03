from flask import Flask, request, Response, make_response
import base64
import io

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename")
    img_data = request.data
    img_bytes = base64.b64decode(img_data)
    img_buffer = io.BytesIO(img_bytes)
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(img_buffer.getvalue())

    return make_response("", 200)
