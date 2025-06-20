from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Decode the base64 encoded string
    decoded_img = base64.b64decode(img_data)

    # Save the image to the specified directory and file name
    path = f"../assets/img/{filename}.png"
    with open(path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
