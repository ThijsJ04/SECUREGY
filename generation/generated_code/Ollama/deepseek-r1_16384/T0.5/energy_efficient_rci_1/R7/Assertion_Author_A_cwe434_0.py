from flask import Flask, request, Response, jsonify
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
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    # Sanitize the filename to avoid path traversal or invalid characters
    import re

    allowed_chars = re.compile(r"^[a-zA-Z0-9_\-\.]+$")
    sanitized_filename = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", filename)

    if not img_data:
        return Response("Missing image data", status=400)

    try:
        # Decode the base64 encoded string
        decoded_img = base64.b64decode(img_data)

        # Save the file to the specified location
        import os

        directory = "../assets/img/"
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        filepath = os.path.join(directory, f"{sanitized_filename}.png")
        with open(filepath, "wb") as f:
            f.write(decoded_img)

        # Return success response
        return jsonify({"message": "Image uploaded successfully"}), 200

    except Exception as e:
        return Response(f"Error uploading image: {str(e)}", status=500)


if __name__ == "__main__":
    app.run(debug=True)
