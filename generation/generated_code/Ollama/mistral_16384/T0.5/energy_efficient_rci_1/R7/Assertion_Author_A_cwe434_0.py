from flask import Flask, request, Response, make_response
import base64
import io

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_data = request.data
    img_bytes = base64.b64decode(img_data)

    with io.BytesIO(img_bytes) as output:
        output.name = f"../assets/img/{filename}.png"
        output.seek(0)
        with open(output, "wb") as out_file:
            out_file.write(output.read())

    return make_response(Response(), 200)
