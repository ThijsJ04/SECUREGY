from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Decode the base64 image data
        decoded_data = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image to file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_data)

        return Response("Image uploaded successfully", status=200)
    except Exception as e:
        return Response(f"Error uploading image: {str(e)}", status=500)
