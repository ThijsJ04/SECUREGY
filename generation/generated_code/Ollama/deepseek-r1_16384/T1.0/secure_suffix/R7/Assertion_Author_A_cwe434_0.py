from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Decode the base64 image data
        decoded_image = base64.b64decode(img_data)

        # Ensure directory exists
        directory = os.path.dirname("../assets/img/")
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Save the file
        filepath = f"../assets/img/{filename}.png"
        with open(filepath, "wb") as f:
            f.write(decoded_image)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(f"Error saving image: {str(e)}", status=500)
