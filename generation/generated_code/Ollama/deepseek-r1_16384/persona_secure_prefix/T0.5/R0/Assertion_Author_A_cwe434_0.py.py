from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = request.args.get('img', '')

    if not filename or not img_data:
        return Response('Missing parameters', 400)

    allowed_chars = re.compile(r'^[a-zA-Z0-9_.-]+$')
    if not allowed_chars.match(filename):
        return Response('Invalid filename', 400)

    try:
        decoded_img = base64.b64decode(img_data)
    except base64.binascii.Error:
        return Response('Invalid base64 data', 400)

    dir_path = os.path.join(app.root_path, '../assets/img')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f'{filename}.png')

    with open(file_path, 'wb') as f:
        f.write(decoded_img)

    return Response('Image uploaded successfully', 200)