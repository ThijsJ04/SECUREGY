from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    data = request.data
    if not data:  # check if a file was actually sent
        return "No file provided", 400

    filename = (
        request.form["filename"] or "unknown"
    )  # provide default filename when not specified in form
    base64_img = base64.b64decode(data)

    try:
        with open("../assets/img/{}.png".format(filename), "wb") as f:
            f.write(base64_img)
    except Exception as e:
        print(
            "Error saving image:", str(e)
        )  # log any errors that may occur during saving the file
        return "An error occurred while saving the image", 500

    return "Image saved successfully", 200
