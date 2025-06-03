from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Extract filename and img parameters from request
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        # Decode the base64 encoded image data
        decoded_image = base64.b64decode(img_data)

        # Save the image to the specified directory and filename
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_image)

        return Response(status=200)
    except Exception as e:
        print(f"Error processing upload: {e}")
        return Response(status=500)
