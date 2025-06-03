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
    # Get filename and img data from request
    if request.form:
        filename = request.form.get("filename")
        img_data = request.form.get("img")
    else:
        filename = request.json.get("filename")
        img_data = request.json.get("img")

    try:
        # Decode base64 string to bytes
        img_bytes = base64.b64decode(img_data)

        # Sanitize the filename
        allowed_chars = set(
            "_"
            + "".join(
                [
                    a
                    for a in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                ]
            )
        )
        filename = "".join(c if c in allowed_chars else "_" for c in filename).lower()

        # Ensure directory exists
        dir_path = os.path.dirname(os.path.abspath(f"../assets/img/{filename}.png"))
        os.makedirs(dir_path, exist_ok=True)

        # Save the image file
        file_path = os.path.join("..", "assets", "img", f"{filename}.png")
        with open(file_path, "wb") as f:
            f.write(img_bytes)

    except Exception as e:
        print(f"Error uploading image: {e}")
        return Response("", status=500)

    return Response("Image uploaded successfully.", status=200)


if __name__ == "__main__":
    app.run(debug=True)
