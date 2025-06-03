import os
from PIL import Image
import io, base64


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get("filename")
    img_str = request.form["img"]
    img_data = base64.decodebytes(img_str)
    tmp_img = Image.open(io.BytesIO(img_data))
    save_path = os.path.join(
        os.path.dirname(__file__), "..", "assets", "img", f"{filename}.png"
    )
    tmp_img.save(save_path)
    return Response(status=200)
