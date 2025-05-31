import os
from io import BytesIO
from PIL import Image

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_b64 = request.args.get('img')

    img_data = base64.decodestring(img_b64)
    img_file = BytesIO(img_data)
    img = Image.open(img_file)
    img.save(f'../assets/img/{filename}.png')

    return Response(status=200)