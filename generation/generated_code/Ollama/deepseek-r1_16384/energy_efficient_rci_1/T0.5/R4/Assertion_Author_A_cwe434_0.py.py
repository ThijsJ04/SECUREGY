from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_b64 = request.args.get('img')

    if not filename or not img_b64:
        return Response("Missing parameters", status=400)

    try:
        img_data = base64.b64decode(img_b64)
    except Exception as e:
        return Response(f"Error decoding image: {str(e)}", status=500)

    save_dir = '../assets/img'
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f'{filename}.png')

    with open(file_path, 'wb') as f:
        f.write(img_data)

    return Response("Image uploaded successfully", status=200)