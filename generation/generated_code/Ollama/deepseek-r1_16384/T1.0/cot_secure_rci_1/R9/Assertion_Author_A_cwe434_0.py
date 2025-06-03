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

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Replace any spaces in base64 string (common URL encoding issue)
        img_bytes = base64.b64decode(img_data.replace("+", " "))

        # Create the directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image file
        filepath = f"../assets/img/{filename}.png"
        with open(filepath, "wb") as f:
            f.write(img_bytes)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


if __name__ == "__main__":
    app.run(debug=True)
