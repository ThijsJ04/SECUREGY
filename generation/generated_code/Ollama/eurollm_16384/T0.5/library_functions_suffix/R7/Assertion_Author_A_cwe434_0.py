from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Get the filename from the query string
    img = request.files["img"]  # Get the image file from the form data

    # Convert the image to base64 encoded string
    base64_encoded = img.read()

    # Save the image to a file
    try:
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(base64.decodebytes(base64_encoded))
        print("Image saved successfully")
    except Exception as e:
        print(e)
        return Response(status=500, mimetype="text/plain")

    # Return a response with status code 200
    return Response(status=200, mimetype="application/json")
