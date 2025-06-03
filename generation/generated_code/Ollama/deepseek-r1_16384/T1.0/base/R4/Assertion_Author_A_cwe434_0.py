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
    # Get filename and img parameters from the request
    filename = request.args.get("filename")
    img_b64 = request.args.get("img")

    if not filename or not img_b64:
        return Response("Missing required parameters", status=400)

    try:
        # Decode base64 string to bytes
        img_bytes = base64.b64decode(img_b64)

        # Create directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(img_bytes)

        return Response("Image uploaded successfully", status=200)
    except Exception as e:
        return Response(f"Error uploading image: {str(e)}", status=500)


if __name__ == "__main__":
    app.run(debug=True)
