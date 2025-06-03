from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    if request.method == "POST":
        filename = request.form["filename"]
        image_data = base64.b64decode(
            request.files["img"].read()
        )  # assuming image file is in the request file part
        data_path = f"../assets/img/{filename}.png"
        with open(data_path, "wb") as output:
            output.write(image_data)
    return Response(status=200)
