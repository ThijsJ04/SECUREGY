from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request
    filename = request.args.get("filename")
    img_data = request.files["img"]  # Assuming the image is being sent in the form data

    # Use base64 to decode the "img" parameter
    try:
        img_data_b64 = img_data.read()
        decoded_img_data = base64.decodestring(img_data_b64)
    except AttributeError:
        return "", 500  # Image not found in the request

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        decoded_img = decoded_img_data.decode("utf-8")
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)
    except Exception as e:
        print(e)
        return "", 500  # Failed to save the image

    return Response("Image uploaded successfully", mimetype="image/png")
