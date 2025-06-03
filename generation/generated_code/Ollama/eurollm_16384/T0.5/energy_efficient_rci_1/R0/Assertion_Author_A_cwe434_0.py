from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    filename = request.form["filename"]
    img = request.files[
        "img"
    ]  # Assuming the image is being sent as a file in the form data

    # Use base64 to decode the "img" parameter.
    try:
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(base64.decodebytes(img.read()))
    except Exception as e:
        print("Error saving image:", str(e))
        return Response(response=str(e), status=500)

    # Return a response with status code equals to 200.
    return Response(status=200)
