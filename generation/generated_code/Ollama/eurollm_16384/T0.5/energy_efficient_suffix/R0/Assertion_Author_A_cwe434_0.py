from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    data = request.get_json()
    filename = data["filename"]
    img_data = request.files["img"]

    # Use base64 to decode the "img" parameter.
    img_data_decoded = base64.b64decode(img_data)

    # Save the image to the file "../assets/img/{filename}.png".
    try:
        with open("../assets/img/" + filename + ".png", "wb") as f:
            f.write(img_data_decoded)
    except Exception as e:
        print(e)
        return Response("Error saving image", status=500, mimetype="text/plain")

    # Return a response with status code equals to 200.
    return Response("Image saved successfully", status=200, mimetype="application/json")
