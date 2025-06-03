from flask import request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form["filename"]
    data = request.files["img"]

    # Get the content-type of the file to determine if it's an image or not
    if "image/jpeg" in data.content_type:
        # Decode the base64 string into a binary format
        decoded_data = base64.b64decode(data)

        # Save the image to a file
        with open("../assets/img/{}.png".format(filename), "wb") as f:
            f.write(decoded_data)
    else:
        return Response("Invalid file type", status=400, mimetype="application/json")

    # Return a success response
    return Response("", status=200)
