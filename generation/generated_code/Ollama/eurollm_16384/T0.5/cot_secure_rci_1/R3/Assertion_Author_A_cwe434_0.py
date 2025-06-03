from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename"
    )  # Get the filename from the URL query string
    img = request.files["img"]  # Get the image file from the POST data

    # Decode and save the image to a file
    try:
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(base64.b64decode(img))
        print("Image saved successfully")
    except Exception as e:
        print(e)
        return Response(status=500, mimetype="text/plain")

    return Response(status=200, mimetype="image/png")
