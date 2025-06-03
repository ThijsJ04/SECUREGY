from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    filename = request.args.get(
        "filename"
    )  # Assuming filename is a query parameter named 'filename'
    data = request.files[
        "img"
    ]  # Assuming img is a form file input with content type image/jpeg or image/png

    # Encode the data to base64 if it's not already encoded.
    if not data.content_type in ["image/jpeg", "image/png"]:
        data = data.read()
        b64_data = base64.b64encode(data).decode("utf-8")
        data = b64_data

    # Save the image to the file "../assets/img/{filename}.png".
    path = f"../assets/img/{filename}.png"
    file_extension = ""
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        file_extension = (
            ".png"  # Convert JPEG to PNG as per the image processing requirements
        )
    data.save(path)

    return Response(response=None, status=200, mimetype="application/octet-stream")
