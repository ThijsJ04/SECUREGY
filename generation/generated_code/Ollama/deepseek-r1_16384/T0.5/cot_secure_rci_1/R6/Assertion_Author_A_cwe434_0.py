from flask import Flask, request, Response
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
    img_data = request.args.get("img", "")

    # Ensure that the filename is safe
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    cleaned_filename = "".join(c if c in allowed_chars else "_" for c in filename)

    # Decode base64 data
    try:
        image_bytes = base64.b64decode(img_data)
    except:
        raise ValueError("Invalid base64 data")

    # Save the image file
    import os

    directory = "../assets/img"
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    filepath = os.path.join(directory, f"{cleaned_filename}.png")
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    # Return response
    from flask import make_response

    return make_response("Image uploaded successfully", 200)


if __name__ == "__main__":
    app.run()
