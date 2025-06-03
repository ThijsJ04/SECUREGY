from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    try:
        # Get the "filename" from the request
        filename = request.args.get("filename")

        # Get the image data from the request (as a string)
        img_data = base64.b64decode(request.form["img"])

        # Save the image to the file "../assets/img/{filename}.png"
        with open("../assets/img/" + filename, "wb") as f:
            f.write(img_data)
    except Exception as e:
        print("Error saving image: ", str(e))

    return Response(status=200)
