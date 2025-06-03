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
    # Get filename and img_data from request parameters
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    try:
        # Decode base64 data
        decoded_image = base64.b64decode(img_data)

        # Create directory if not exists
        import os

        os.makedirs("../assets/img", exist_ok=True)

        # Save image to file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_image)

        # Return success response
        return Response("Image uploaded successfully", status=200)

    except Exception as e:
        # Handle exceptions and return error responses
        if not filename or not img_data:
            return Response("Missing parameters", status=400)
        if "is a directory" in str(e):
            return Response("File path is invalid", status=400)
        return Response(str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True)
