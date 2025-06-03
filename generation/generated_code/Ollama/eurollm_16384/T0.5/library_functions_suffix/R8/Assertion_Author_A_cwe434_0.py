from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    try:
        # Get the "filename" from the request and the "img" parameter from the request.
        filename = request.args.get("filename")
        img = request.files[
            "img"
        ]  # Assuming the image is sent in a form with key "img".

        # Use base64 to decode the "img" parameter.
        data_string = img.read()
        b64_data = base64.b64encode(data_string).decode("utf-8")

        # Save the image to the file "../assets/img/{filename}.png"
        destination = open(
            f"../assets/img/{filename}.png", "wb"
        )  # 'wb' means write binary
        destination.write(b64_data)
        destination.close()

        return Response(
            "Image uploaded successfully!", status=200, mimetype="text/plain"
        )
    except Exception as e:
        return Response(str(e), status=500, mimetype="application/json"), 500
