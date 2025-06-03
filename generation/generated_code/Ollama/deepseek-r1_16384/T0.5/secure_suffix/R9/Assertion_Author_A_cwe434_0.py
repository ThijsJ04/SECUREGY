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
    # Extract filename and img parameters from request arguments
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(
            '{"status": "error", "message": "Missing required parameters"}',
            status=400,
            mimetype="application/json",
        )

    # Ensure the filename is valid and prevent path traversal
    safe_filename = os.path.join("assets/img", os.path.basename(filename))

    try:
        # Decode base64 data
        decoded_img = base64.b64decode(img_data)

        # Save image to file
        with open(f"../{safe_filename}.png", "wb") as f:
            f.write(decoded_img)

        return Response(
            '{"status": "success", "message": "Image uploaded successfully"}',
            status=200,
            mimetype="application/json",
        )
    except base64.binascii.Error:
        return Response(
            '{"status": "error", "message": "Invalid base64 data"}',
            status=400,
            mimetype="application/json",
        )
    except Exception as e:
        return Response(
            '{"status": "error", "message": "Internal server error"}',
            status=500,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run(debug=True)
