from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request
    filename = request.form.get("filename")
    print("Filename:", filename)

    # Get the "img" parameter from the request (as a base64 encoded string)
    img_data = request.data

    # Decode the base64-encoded image data using base64.b64decode()
    try:
        img = base64.b64decode(img_data).decode("utf-8")
        print("Image data:", img)
    except Exception as e:
        print("Error decoding image:", str(e))
        return Response(status=500)

    # Save the image to a file
    try:
        with open("../assets/img/" + filename, "wb") as f:
            f.write(img)
        print("Image saved successfully.")
    except Exception as e:
        print("Error saving image:", str(e))
        return Response(status=500)

    # Return a response with status code 200
    return Response(status=200, mimetype="image/png")
