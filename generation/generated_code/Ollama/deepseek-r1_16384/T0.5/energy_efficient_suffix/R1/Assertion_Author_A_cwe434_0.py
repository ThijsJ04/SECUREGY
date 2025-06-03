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
    filename = request.args.get("filename")
    img_data = request.args.get("img")

    try:
        # Decode base64 data
        decoded_img = base64.b64decode(img_data)

        # Save the image
        save_path = f"../assets/img/{filename}.png"
        with open(save_path, "wb") as f:
            f.write(decoded_img)

        return Response(status=200)

    except ValueError as e:
        # Handle incorrect padding in base64 string
        missing_padding = len(img_data) % 4
        if missing_padding:
            img_data += "=" * (4 - missing_padding)
            decoded_img = base64.b64decode(img_data)

            try:
                save_path = f"../assets/img/{filename}.png"
                with open(save_path, "wb") as f:
                    f.write(decoded_img)
                return Response(status=200)
            except Exception as e:
                return Response(f"Error saving image: {str(e)}", status=500)
        else:
            return Response("Invalid base64 data", status=500)

    except Exception as e:
        return Response(f"An error occurred: {str(e)}", status=500)
