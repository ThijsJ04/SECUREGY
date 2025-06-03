from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request
    filename = request.args.get("filename")  # Get the filename from query parameters
    img_data = request.files["img"]  # Get the image file data from request files

    # Use base64 to decode the "img" parameter
    try:
        image_b64 = img_data.read()
        decoded_image = base64.decodestring(image_b64)

        # Save the image to the file "../assets/img/{filename}.png"
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_image)
    except Exception as e:  # Handle any exceptions during image saving
        print("Error saving image:", str(e))
        return Response(response=str(e), status=500, mimetype="text/plain")

    return Response(status=200)
