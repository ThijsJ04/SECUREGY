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
    img_data = request.args.get("img")

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except:
        return Response(status=500)

    safe_filename = filename.strip().replace("/", "_").replace("\\", "_")

    save_path = f"../assets/img/{safe_filename}.png"

    try:
        with open(save_path, "wb") as img_file:
            img_file.write(decoded_img)
    except Exception as e:
        app.logger.error(f"Error saving image: {e}")
        return Response(status=500)

    return Response()
