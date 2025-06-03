from flask import request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    filename = request.form.get("filename")  # Get the "filename" from the form data
    img = request.files["img"]  # Get the "img" parameter from the request (as a file)
    print(f"Filename: {filename}, Image: {img}")

    if not os.path.exists("../assets/img"):
        os.makedirs("../assets/img")  # Create the assets folder if it doesn't exist

    data = img.read()  # Read the contents of the file
    filename_parts = filename.split(".")[-1]  # Get the file extension (e.g., .png)
    with open(
        f"../assets/img/{filename}.{filename_parts}", "wb"
    ) as f:  # Save the image to a file
        f.write(data)
    print("Image saved successfully!")

    return Response(status=200, mimetype="image/png")
