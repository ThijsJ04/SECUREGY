import flask, base64
from io import BytesIO

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
    img_data = request.values.get("img")
    decoded_img = base64.b64decode(img_data)
    img_buffer = BytesIO(decoded_img)
    with open(f"../assets/img/{filename}.png", "wb") as out:
        out.write(img_buffer.getvalue())

    return flask.Response(status=200)
