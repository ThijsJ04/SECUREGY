import os
from io import BytesIO

def upload_img():
    filename = request.args.get('filename')
    img = request.args.get('img')
    decoded_img = base64.b64decode(img)
    output_file = f"../assets/img/{filename}.png"
    with open(output_file, "wb") as f:
        f.write(decoded_img)
    return Response(status=200)