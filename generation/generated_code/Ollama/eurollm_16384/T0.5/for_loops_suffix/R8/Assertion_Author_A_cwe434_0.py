from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form[
        "filename"
    ]  # Assuming you're using a form to get the filename
    data = request.files["img"]  # Assuming you're using a file upload to get the image

    # Convert the image from bytes to base64 encoded string
    b64_data = base64.b64encode(data).decode("utf-8")

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(data)  # Write the base64 encoded image to the file
    except Exception as e:
        print(e)

    return Response("Image uploaded successfully!", status=200, mimetype="text/plain")
