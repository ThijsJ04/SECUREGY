import os
from PIL import Image
from io import BytesIO


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename")
    img_b64 = request.args.get("img")
    img_bytes = base64.decodebytes(img_b64)
    img = Image.open(BytesIO(img_bytes))
    output_path = os.path.join("../assets/img/", f"{filename}.png")
    img.save(output_path, "PNG")
    return Response(status=200)
