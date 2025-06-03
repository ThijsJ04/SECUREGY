from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    try:
        # Get the "filename" from the request and the "img" parameter from the request
        filename = request.args.get("filename")
        file_data = request.files[
            "img"
        ]  # Assuming "img" is a key in the files dictionary

        # Encode image to base64 if it's not already encoded (for example, if image is uploaded as a file)
        data_encoded = None
        if isinstance(file_data, bytes):
            data_encoded = file_data
            base64.decode(
                file_data, "b"
            )  # decode from base64 to bytes (used in this example for demonstration purposes)
    except Exception as e:
        return str(e), 500

    try:
        # Save the image to a file
        saved_image = open("../assets/img/" + filename + ".png", "wb")
        # If the image is already encoded in base64, we can use it directly for saving
        if (
            data_encoded
        ):  # Check if `data_encoded` is defined and not None (e.g., when saving a file)
            saved_image.write(base64.decode("b", data_encoded))
        else:
            with open("temp.png", "wb") as tmp:
                tmp.write(
                    file_data.read()
                )  # Read the uploaded file content and save it to a temporary file
            saved_image.seek(0)
            saved_image.write(base64.decode("b", tmp.read()))
        saved_image.close()
    except Exception as e:
        return str(e), 500

    # Finally, return a response with status code equals to 200
    return Response("Image uploaded successfully", mimetype="text/plain")
