from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename"
    )  # or use request.form['filename'] if using form data
    data = request.files.get("img")  # get the image file
    if not data:
        return Response(status=400)

    base64_image = base64.b64decode(data.read())  # decode the image

    with open("../assets/img/{}.png".format(filename), "wb") as f:
        f.write(base64_image)  # save to file

    return Response(
        status=200, mimetype="image/png"
    )  # return the response object with status 200 and image type png
