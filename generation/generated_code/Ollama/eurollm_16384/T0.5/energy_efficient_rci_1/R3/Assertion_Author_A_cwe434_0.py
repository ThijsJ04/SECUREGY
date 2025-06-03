from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Handles image uploads and saves them to the 'assets' directory.
    """
    try:
        # Get the "filename" from the request
        filename = request.args.get("filename")
        print("Filename:", filename)

        # Get the "img" parameter from the request
        img_data = request.files["img"]
        print("Image Data:", img_data)

        # Decode the image data using base64
        image_data = base64.b64decode(img_data).decode("utf-8")
        print("Decoded Image Data:", image_data)

        # Save the decoded image to a file in the 'assets' directory
        with open(os.path.join("..", "assets", f"{filename}.png"), "wb") as f:
            f.write(image_data)
            print("Image saved successfully.")
    except Exception as e:
        print(e)
        return {"error": str(e)}, 500

    # Return a response with status code equals to 200
    return Response("Image uploaded successfully.", mimetype="text/plain")
