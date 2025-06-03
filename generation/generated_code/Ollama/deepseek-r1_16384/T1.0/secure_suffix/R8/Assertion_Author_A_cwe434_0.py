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
    # Get filename and img_data from request arguments
    filename = request.args.get("filename")
    img_data = request.args.get("img", "")

    if not filename or not img_data:
        return Response("Missing required parameters", status=400)

    try:
        # Decode the base64 encoded image data
        decoded_data = base64.b64decode(img_data, validate=True)

        # Ensure directory exists
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image to file
        with open(f"../assets/img/{filename}.png", "wb") as f:
            f.write(decoded_data)

        return Response("Image uploaded successfully", status=200)
    except base64.binascii.Error as e:
        return Response("Invalid base64 data", status=415)
    except (IOError, PermissionError) as e:
        return Response(f"Failed to save file: {str(e)}", status=500)
    except Exception as e:
        return Response("Internal server error", status=500)


if __name__ == "__main__":
    app.run(debug=True)
