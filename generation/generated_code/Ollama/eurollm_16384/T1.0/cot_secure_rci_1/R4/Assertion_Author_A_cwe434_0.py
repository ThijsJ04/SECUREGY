from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]  # Get the filename from form data
    img_data = request.files["img"].read()  # Read the image data from file
    decoded_img = base64.b64decode(img_data)  # Decode the image using base64

    with open(f"../assets/img/{filename}.png", "wb") as f:  # Save the image to file
        f.write(decoded_img)

    return Response(status=200, mimetype="image/png")
