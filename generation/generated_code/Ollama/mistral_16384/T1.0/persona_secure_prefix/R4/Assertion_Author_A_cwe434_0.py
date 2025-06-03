from io import BytesIO
import os

...


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", "")
    img_data = request.form["img"]
    img_decoded = base64.b64decode(img_data)
    img_buffer = BytesIO(img_decoded)
    image_path = os.path.join("../assets/img", f"{filename}.png")
    with open(image_path, "wb") as out:
        img_buffer.seek(0)
        out.write(img_buffer.read())
    return Response(status=200)
