from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Get the "filename" from the request
    if not filename:
        return "Error: Missing filename", 400

    img_data = request.files["img"]  # Get the "img" parameter from the request
    decoded_img = base64.b64decode(img_data)  # Decode the "img" parameter using base64

    with open(f"../assets/img/{filename}.png", "wb") as f:  # Save the image to a file
        f.write(decoded_img)

    return Response("Image saved successfully!", status=200, mimetype="image/png")
