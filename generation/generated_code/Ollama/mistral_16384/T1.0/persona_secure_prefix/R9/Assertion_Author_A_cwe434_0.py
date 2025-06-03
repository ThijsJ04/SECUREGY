import os
from io import BytesIO


@app.route("/img/upload")
def upload_img():
    filename = request.args.get("filename", None)
    img_data = request.values.get("img", None)

    if not filename or not img_data:
        return Response(status=400)  # Bad Request

    try:
        img_data = base64.decodebytes(img_data.encode())
    except Exception as e:
        return Response(response=str(e), status=500)  # Internal Server Error

    filepath = os.path.join("../assets/img", f"{filename}.png")

    with open(filepath, "wb") as fh:
        fh.write(img_data)

    return Response(status=200)  # OK
