from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form["filename"]  # Assuming the filename is a form parameter
    img = request.files["img"]  # Assuming the image is a file parameter

    if not img:
        return Response(status=400, mimetype="application/json")

    data_bytes = img.read()  # Read the image bytes
    decoded_data = base64.b64decode(data_bytes)  # Decode the base64-encoded data
    img_type, img_string = img.split(
        ","
    )  # Split the image string into type and content

    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_data)  # Write the decoded data to a file

    return Response(status=200, mimetype="application/json")
