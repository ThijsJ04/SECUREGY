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
    filename = request.values.get("filename")
    img_data = request.values.get("img")

    if not filename or not img_data:
        return Response(status=400)

    allowed_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    )
    if not all(c in allowed_chars for c in filename):
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        file_path = f"../assets/img/{filename}.png"
        with open(file_path, "wb") as f:
            f.write(decoded_img)
        return Response(status=200)
    except Exception as e:
        print(f"Error processing image: {e}")
        return Response(status=500)


if __name__ == "__main__":
    app.run(debug=True)
