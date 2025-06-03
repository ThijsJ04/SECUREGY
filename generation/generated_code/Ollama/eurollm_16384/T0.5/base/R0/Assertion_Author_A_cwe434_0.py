from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", default=None)  # optional parameter
    if filename:
        # Get the img parameter from the request
        data = request.data
        # Use base64 to decode the img parameter
        img_bytes = base64.b64decode(data).decode(
            "utf-8"
        )  # this may not work for all types of images
        # Save the image to the file "../assets/img/{filename}.png"
        try:
            with open("./static/img/" + filename, "wb") as f:
                f.write(img_bytes)
        except Exception as e:
            print(e)  # handle any exceptions that might occur during file saving
    return Response("Image uploaded successfully", status=200)
