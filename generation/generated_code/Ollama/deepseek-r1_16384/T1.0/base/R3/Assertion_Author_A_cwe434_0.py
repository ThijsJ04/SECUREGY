from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get filename and image data from request arguments
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)  # Return 400 Bad Request if parameters are missing

    try:
        # Decode base64 data
        decoded_img = base64.b64decode(img_data)

        # Ensure the directory exists
        os.makedirs("../assets/img", exist_ok=True)

        # Save image to file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)

        return Response(status=200)  # Return 200 OK response
    except Exception as e:
        print(f"Error saving image: {e}")  # Log any errors
        return Response(
            status=500
        )  # Return 500 Internal Server Error if something goes wrong
