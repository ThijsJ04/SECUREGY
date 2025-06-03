from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename", "default_filename")
    img_data = request.args.get("img", "") or request.form.get("img", "")

    # Remove data URL prefix if present
    if img_data.startswith("data:image/png;base64,"):
        img_data = img_data.split(",")[1]

    try:
        decoded_img = base64.b64decode(img_data)
        filepath = os.path.join("../assets/img/", f"{filename}.png")
        with open(filepath, "wb") as f:
            f.write(decoded_img)
        return Response("", 200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response("Error processing image", 500)


if __name__ == "__main__":
    app.run()
