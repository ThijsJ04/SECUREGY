from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")  # Get the "filename" from the query string
    data = (
        request.data
    )  # Get the image data from the request body (not applicable for GET requests)
    if not filename:
        return Response(
            status=400,
            mimetype="application/json",
            headers={"Content-Type": "application/json"},
        )
    try:
        decoded_data = base64.b64decode(data).decode(
            "utf-8"
        )  # Decode the image data using base64
        img = Image.open(io.BytesIO(decoded_data))
    except Exception as e:
        return Response(
            status=500,
            mimetype="application/json",
            headers={"Content-Type": "application/json"},
            data={"error": str(e)},
        )
    filename = os.path.join(
        "..", "assets", "img", filename + ".png"
    )  # Save the image to the specified directory
    img.save(filename)
    return Response(
        status=200,
        mimetype="application/json",
        headers={"Content-Type": "application/json"},
        data={"message": "Image saved successfully"},
    )
