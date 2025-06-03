from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    try:
        # Get the "filename" from the request and the "img" parameter from the request.
        file = request.files["img"]
        filename = file.filename
        print("Uploaded File : ", filename)
        # Use base64 to decode the "img" parameter.
        data = base64.b64decode(file.read())
    except:
        pass  # Handle exceptions for file upload if necessary
