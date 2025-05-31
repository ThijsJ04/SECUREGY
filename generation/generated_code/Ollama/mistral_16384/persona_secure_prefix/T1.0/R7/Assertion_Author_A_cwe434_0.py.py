from io import BytesIO
import os

def upload_img():
    filename = request.args.get('filename')
    img = request.args.get('img', type=str, default=None)

    if not img:
        return Response(status=400)

    img_bytes = base64.b64decode(img)
    temp_img = BytesIO(img_bytes)

    filepath = f"../assets/img/{filename}.png"
    with open(filepath, 'wb') as f:
        f.write(temp_img.getvalue())

    return Response(status=200)