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
    filename = request.form.get("filename")
    img_data = request.form.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        save_path = f"../assets/img/{filename}.png"
        with open(save_path, "wb") as f:
            f.write(decoded_img)
        return Response(status=200)
    except Exception as e:
        print(f"Error processing image upload: {e}")
        return Response(status=500)
