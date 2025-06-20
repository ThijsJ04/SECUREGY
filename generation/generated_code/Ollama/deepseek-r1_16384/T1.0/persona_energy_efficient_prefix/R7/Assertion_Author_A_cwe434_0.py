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
        return Response(json.dumps({"error": "Missing parameters"}), status=400)

    try:
        # Create directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Decode base64 data and save file
        decoded_data = base64.b64decode(img_data)
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_data)

        return Response(
            json.dumps({"message": "Image uploaded successfully"}),
            status=200,
            content_type="application/json",
        )

    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)


if __name__ == "__main__":
    app.run(debug=True)
