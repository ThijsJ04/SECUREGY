from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename"
    )  # Get the filename parameter from the request
    data = request.data  # Get the image data from the request

    # Decode the image data using base64
    img_data = base64.b64decode(data)

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        with open("../assets/img/" + filename + ".png", "wb") as f:
            f.write(img_data)
    except Exception as e:
        print(e)  # Handle any exceptions that may occur during file writing

    return Response("Image uploaded successfully", status=200, mimetype="text/plain")
