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
    filename = request.args.get("filename", "")
    img_data = request.args.get("img", "")

    # Ensure the filename is safe
    filename = os.path.join("assets/img", filename)
    filename = os.path.normpath(filename)  # Normalize path
    filename = os.path.basename(filename)  # Get just the filename

    try:
        # Decode base64 data, handling possible padding issues
        img_bytes = base64.urlsafe_b64decode(img_data)

        # Save image to file
        with open(f"../{filename}.png", "wb") as f:
            f.write(img_bytes)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)


if __name__ == "__main__":
    app.run(debug=True)
