from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    # Extract filename and img from the request
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    # Validate the filename to prevent directory traversal
    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    clean_filename = "".join([c if c in allowed_chars else "_" for c in filename])

    # Decode base64 data and handle padding issues
    img_bytes = base64.b64decode(img_data + "=" * ((4 - len(img_data) % 4) % 4))

    # Save the image to the specified directory
    file_path = f"../assets/img/{clean_filename}.png"
    with open(file_path, "wb") as f:
        f.write(img_bytes)

    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True)
