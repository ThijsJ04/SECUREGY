from io import BytesIO
import os

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_b64 = request.args.get('img')

    img_data = base64.b64decode(img_b64)
    img_buf = BytesIO(img_data)

    save_path = os.path.join('../assets/img', filename + '.png')
    with open(save_path, 'wb') as f:
        f.write(img_buf.getvalue())

    return Response(status=200)