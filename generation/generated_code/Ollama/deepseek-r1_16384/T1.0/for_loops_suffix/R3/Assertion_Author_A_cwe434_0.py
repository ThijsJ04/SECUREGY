from flask import Flask, request, Response, jsonify
import base64
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    try:
        # Extract filename and img data from the request
        filename = request.form.get("filename", "")
        img_data = request.form.get("img", "")

        if not filename or not img_data:
            return Response("Missing parameters", status=400)

        # Decode base64 string to bytes
        img_bytes = base64.b64decode(img_data)

        # Ensure directory exists
        dir_path = os.path.join(os.path.dirname(__file__), "..", "assets", "img")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Save the image to file
        filepath = os.path.join(dir_path, f"{filename}.png")
        with open(filepath, "wb") as f:
            f.write(img_bytes)

        return Response("Image saved successfully", status=200)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error saving image: {str(e)}")
        return jsonify({"error": "Failed to save image"}), 500


if __name__ == "__main__":
    app.run(debug=True)
