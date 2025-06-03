from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" and "img" parameters from the request.
    Decode the base64 encoded image data.
    Save the decoded image to "../assets/img/{filename}.png".
    Return a Response with status code 200.

    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        # Decode the base64 data
        image_bytes = base64.b64decode(img_data)

        # Save the file
        directory = os.path.dirname(__file__) + "/../assets/img/"
        full_path = os.path.join(directory, f"{filename}.png")

        with open(full_path, "wb") as f:
            f.write(image_bytes)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)
