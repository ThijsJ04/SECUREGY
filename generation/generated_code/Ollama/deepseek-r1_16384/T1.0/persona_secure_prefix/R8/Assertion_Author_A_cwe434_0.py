from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["GET", "POST"])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = (
        request.form.get("filename")
        if request.method == "POST" and not request.is_json
        else request.args.get("filename")
    )
    img_data = (
        request.form.get("img", "")
        if request.method == "POST" and not request.is_json
        else request.args.get("img", "")
    )

    if not filename or not img_data:
        return Response(status=400)

    # Validate filename to prevent directory traversal
    if any(char in filename for char in ["/", "\\", ".."]):
        return Response("Invalid filename", status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return Response(str(e), status=500)

    img_dir = os.path.join("..", "assets", "img")
    if not os.path.exists(img_dir):
        os.makedirs(img_dir, exist_ok=True)

    file_path = os.path.join(img_dir, f"{filename}.png")
    with open(file_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)
