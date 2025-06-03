from flask import Flask, request, Response
import base64
import os
import json

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(
            json.dumps({"error": "Missing required parameters"}),
            status=400,
            mimetype="application/json",
        )

    try:
        # Decode the base64 image data
        decoded_img = base64.b64decode(img_data.strip())

        # Ensure directory exists
        os.makedirs("../assets/img", exist_ok=True)

        # Save the file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_img)

        return Response(
            json.dumps({"message": "Image uploaded successfully"}),
            status=200,
            mimetype="application/json",
        )
    except Exception as e:
        return Response(
            json.dumps({"error": str(e)}), status=500, mimetype="application/json"
        )
