from flask import request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming the filename is in a form parameter called 'filename'
    img = request.files["img"]
    data = img.read()

    # Convert the image to bytes using base64
    b64_data = base64.b64encode(data)
    b64_data_str = b64_data.decode("utf-8")

    # Save the decoded image data as a binary file
    saved_file = open("../assets/img/{}.png".format(filename), "wb")
    saved_file.write(b64_data)
    saved_file.close()

    return Response(
        "Image uploaded successfully!", status=200, mimetype="application/json"
    )
