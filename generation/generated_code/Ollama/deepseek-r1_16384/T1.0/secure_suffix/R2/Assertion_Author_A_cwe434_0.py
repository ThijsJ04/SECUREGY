from flask import Flask, request, Response
import base64
import os
import json

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Get filename and img data from request parameters
    if "filename" not in request.args or "img" not in request.args:
        return Response(
            response=json.dumps({"error": "Missing required parameters"}),
            status=400,
            mimetype="application/json",
        )

    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Validate and sanitize the filename
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    clean_filename = "".join([c for c in filename if c in allowed_chars])

    try:
        # Decode the base64 image data
        decoded_data = base64.b64decode(img_data)

        # Create target directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save the file to the specified location
        with open(f"../assets/img/{clean_filename}.png", "wb") as f:
            f.write(decoded_data)

        return Response(
            response=json.dumps({"message": "Image uploaded successfully"}),
            status=200,
            mimetype="application/json",
        )
    except Exception as e:
        return Response(
            response=json.dumps({"error": str(e)}),
            status=500,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run()
